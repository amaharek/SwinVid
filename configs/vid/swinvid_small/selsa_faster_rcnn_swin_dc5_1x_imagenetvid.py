_base_ = [
    './faster_rcnn_swin_small_fpn.py',  # worked 
    './imagenet_vid_fgfa_style.py',
    './default_runtime.py'
]
find_unused_parameters=True
model = dict(
    type='SELSA',
    detector=dict(
        roi_head=dict(
            type='SelsaRoIHead',
            bbox_head=dict(
                type='SelsaBBoxHead',
                num_shared_fcs=2,
                aggregator=dict(
                    type='SelsaAggregator',
                    in_channels=1024,
                    num_attention_blocks=16)))))

# dataset settings
data = dict(
    val=dict(
        ref_img_sampler=dict(
            _delete_=True,
            num_ref_imgs=14,
            frame_range=[-7, 7],
            method='test_with_adaptive_stride')),
    test=dict(
        ref_img_sampler=dict(
            _delete_=True,
            num_ref_imgs=14,
            frame_range=[-7, 7],
            method='test_with_adaptive_stride')))

# optimizer
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(
    _delete_=True, grad_clip=dict(max_norm=35, norm_type=2))
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=1.0 / 3,
    step=[2, 5])
# runtime settings
total_epochs = 7
evaluation = dict(metric=['bbox'], interval=7)
