from keras import backend as K


class Config:

	def __init__(self):

		self.verbose = True

		# setting for data augmentation
		self.use_horizontal_flips = False
		self.use_vertical_flips = False
		self.rot_90 = False

		# anchor box scales
		# self.anchor_box_scales = [128, 256, 512]
		self.anchor_box_scales = [128, 256, 384]

		# anchor box ratios
		self.anchor_box_ratios = [[1, 1], [1, 2], [2, 1]]

		# size to resize the smallest side of the image
		self.im_size = 600

		# image channel-wise mean to subtract
		# self.img_channel_mean = [103.939, 116.779, 123.68]
		self.img_channel_mean = [109.15286235, 109.15286235, 109.15286235]
		self.img_scaling_factor = 1.0

		# number of ROIs at once
	    # self.num_rois = 4
		self.num_rois = 64

		# stride at the RPN (this depends on the network configuration)
		# self.rpn_stride = 16
		self.rpn_stride = 10

		self.balanced_classes = False

		# scaling the stdev
		self.std_scaling = 4.0
		self.classifier_regr_std = [8.0, 8.0, 4.0, 4.0]

		# overlaps for RPN
		self.rpn_min_overlap = 0.3
		self.rpn_max_overlap = 0.7

		# overlaps for classifier ROIs
		self.classifier_min_overlap = 0.1
		self.classifier_max_overlap = 0.5

		# number of epochs for training
		self.num_epochs = 50

		# placeholder for the class mapping, automatically generated by the parser
		self.class_mapping = None

		#location of pretrained weights for the base network 
		# weight files can be found at:
		# https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_th_dim_ordering_th_kernels_notop.h5
		# https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5
		if K.image_dim_ordering() == 'th':
			self.base_net_weights = 'resnet50_weights_th_dim_ordering_th_kernels_notop.h5'
		else:
			# self.base_net_weights = 'resnet50_weights_tf_dim_ordering_tf_kernels.h5
			self.base_net_weights = 'resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'

		self.model_path = 'model_frcnn.hdf5'
		# self.model_path = 'weights.{epoch:02d}-{val_loss:.2f}.hdf5'
