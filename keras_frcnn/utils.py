

def get_img_output_length(width, height):
	def get_output_length(input_length):
		# zero_pad
		input_length += 6
		# apply 4 strided convolutions
		filter_sizes = [7, 3, 1, 1]
		stride = 2
		for filter_size in filter_sizes:
			input_length = (input_length - filter_size + stride) // stride
		return input_length

	return get_output_length(width), get_output_length(height)

def union(au, bu):
	x = min(au[0], bu[0])
	y = min(au[1], bu[1])
	w = max(au[2], bu[2]) - x
	h = max(au[3], bu[3]) - y
	return x, y, w, h

def intersection(ai, bi):
	x = max(ai[0], bi[0])
	y = max(ai[1], bi[1])
	w = min(ai[2], bi[2]) - x
	h = min(ai[3], bi[3]) - y
	if w < 0 or h < 0:
		return 0, 0, 0, 0
	return x, y, w, h

def iou(a, b):
	# a and b should be (x1,y1,x2,y2)
	assert a[0] < a[2]
	assert a[1] < a[3]
	assert b[0] < b[2]
	assert b[1] < b[3]

	i = intersection(a, b)
	u = union(a, b)

	area_i = i[2] * i[3]
	area_u = u[2] * u[3]
	return float(area_i) / float(area_u)


def get_new_img_size(width, height, img_min_side=600):
	if width <= height:
		f = float(img_min_side) / width
		resized_height = int(f * height)
		resized_width = img_min_side
	else:
		f = float(img_min_side) / height
		resized_width = int(f * width)
		resized_height = img_min_side

	return resized_width, resized_height