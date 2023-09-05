APP = helloworld

SRCS-y := main.c

PKGCONF ?= pkg-config

# Build using pkg-config variables if possible
ifneq ($(shell $(PKGCONF) --exists libdpdk && echo 0),0)
  $(error "no installation of DPDK found")
endif

CFLAGS += -O3 $(shell $(PKGCONF) --cflags libdpdk)
LDFLAGS_SHARED = $(shell $(PKGCONF) --libs libdpdk)
LDFLAGS_STATIC = $(shell $(PKGCONF) --static --libs libdpdk)

all: shared static

shared: $(SRCS-y)
	$(CC) $(CFLAGS) $(SRCS-y) -o $(APP)-shared $(LDFLAGS_SHARED)

static: $(SRCS-y)
	$(CC) $(CFLAGS) $(SRCS-y) -o $(APP)-static $(LDFLAGS_STATIC)

clean:
	rm -f $(APP)-*
