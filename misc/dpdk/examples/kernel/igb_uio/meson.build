project('igb_uio-kmod', 'c',
        default_options: ['buildtype=release'])

mkfile = custom_target('igb_uio_makefile',
                       output: 'Makefile',
                       command: ['touch', '@OUTPUT@'])

kernel_source_dir = get_option('kernel_dir')

sources = files(
    'igb_uio.c',
    'Kbuild'
)

custom_target('igb_uio-kmod',
              input: sources,
              output: 'igb_uio.ko',
              command: ['make', '-C', kernel_source_dir,
                        'M=' + meson.current_build_dir(),
                        'src=' + meson.current_source_dir(),
                        'modules'],
              depends: mkfile,
              install: false,
              build_by_default: true)
