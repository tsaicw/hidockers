project('helloworld-app',  # Name of the project
        'c',               # What programming language it uses
        version: '1.0.0',
        license: 'MIT'
)

# sources = 'main.c'
# sources = ['main.c']
sources = files(
    'main.c'
)

dpdk = dependency('libdpdk',                                         # Name of the dependency
                  method: 'pkg-config',                              # Detection method
                  required: true,
                  static: get_option('default_library') == 'static'  # Static / Shared
       )

# Build targets: executable, library, static_library and shared_library
executable('helloworld',       # Name of the executable
           sources,            # Source files
           dependencies: dpdk
)
