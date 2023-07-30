APP = helloworld

SRCS-y := main.c

PKGCONF ?= pkg-config

# Build using pkg-config variables if possible
ifneq ($(shell $(PKGCONF) --exists libdpdk && echo 0),0)
  $(error "no installation of DPDK found")
endif

CFLAGS += -O3 $(shell $(PKGCONF) --cflags libdpdk)
LDFLAGS_SHARED = $(shell $(PKGCONF) --libs libdpdk)

$(APP): $(SRCS-y) Makefile
	$(CC) $(CFLAGS) $(SRCS-y) -o $@ $(LDFLAGS_SHARED)

clean:
	rm -f ${APP}
