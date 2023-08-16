#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
# Source0 file verified with key 0x779B22DFB3E717B7 (roger@atchoo.org)
#
Name     : mosquitto
Version  : 2.0.16
Release  : 49
URL      : https://mosquitto.org/files/source/mosquitto-2.0.16.tar.gz
Source0  : https://mosquitto.org/files/source/mosquitto-2.0.16.tar.gz
Source1  : https://mosquitto.org/files/source/mosquitto-2.0.16.tar.gz.asc
Summary  : mosquitto MQTT library (C bindings)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mosquitto-bin = %{version}-%{release}
Requires: mosquitto-data = %{version}-%{release}
Requires: mosquitto-lib = %{version}-%{release}
Requires: mosquitto-license = %{version}-%{release}
Requires: mosquitto-man = %{version}-%{release}
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libcjson)
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Select appropriate systemd service based on your compile settings. If you
enabled WITH_SYSTEMD, use mosquitto.service.notify, otherwise use
mosquitto.service.simple. The service must be renamed to mosquitto.service
before usage. Don't forget to change default paths in service file if you
changed the default build settings.

%package bin
Summary: bin components for the mosquitto package.
Group: Binaries
Requires: mosquitto-data = %{version}-%{release}
Requires: mosquitto-license = %{version}-%{release}

%description bin
bin components for the mosquitto package.


%package data
Summary: data components for the mosquitto package.
Group: Data

%description data
data components for the mosquitto package.


%package dev
Summary: dev components for the mosquitto package.
Group: Development
Requires: mosquitto-lib = %{version}-%{release}
Requires: mosquitto-bin = %{version}-%{release}
Requires: mosquitto-data = %{version}-%{release}
Provides: mosquitto-devel = %{version}-%{release}
Requires: mosquitto = %{version}-%{release}

%description dev
dev components for the mosquitto package.


%package lib
Summary: lib components for the mosquitto package.
Group: Libraries
Requires: mosquitto-data = %{version}-%{release}
Requires: mosquitto-license = %{version}-%{release}

%description lib
lib components for the mosquitto package.


%package license
Summary: license components for the mosquitto package.
Group: Default

%description license
license components for the mosquitto package.


%package man
Summary: man components for the mosquitto package.
Group: Default

%description man
man components for the mosquitto package.


%prep
%setup -q -n mosquitto-2.0.16
cd %{_builddir}/mosquitto-2.0.16
pushd ..
cp -a mosquitto-2.0.16 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692198189
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}  WITH_SYSTEMD=yes

pushd ../buildavx2
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
make  %{?_smp_mflags}  WITH_SYSTEMD=yes
popd

%install
export SOURCE_DATE_EPOCH=1692198189
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mosquitto
cp %{_builddir}/mosquitto-%{version}/edl-v10 %{buildroot}/usr/share/package-licenses/mosquitto/86efdc5056a6e2e60451a6947ad69923744203b9 || :
pushd ../buildavx2/
%make_install_v3 prefix=/usr LIB_SUFFIX=64
popd
%make_install prefix=/usr LIB_SUFFIX=64
## install_append content
mkdir -p %{buildroot}/usr/share/mosquitto
mv %{buildroot}/etc/mosquitto/* %{buildroot}/usr/share/mosquitto/
rmdir %{buildroot}/etc/mosquitto %{buildroot}/etc
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/mosquitto
/V3/usr/bin/mosquitto_ctrl
/V3/usr/bin/mosquitto_passwd
/V3/usr/bin/mosquitto_pub
/V3/usr/bin/mosquitto_rr
/V3/usr/bin/mosquitto_sub
/usr/bin/mosquitto
/usr/bin/mosquitto_ctrl
/usr/bin/mosquitto_passwd
/usr/bin/mosquitto_pub
/usr/bin/mosquitto_rr
/usr/bin/mosquitto_sub

%files data
%defattr(-,root,root,-)
/usr/share/mosquitto/aclfile.example
/usr/share/mosquitto/mosquitto.conf.example
/usr/share/mosquitto/pskfile.example
/usr/share/mosquitto/pwfile.example

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/mosquitto_dynamic_security.so
/usr/include/mosquitto.h
/usr/include/mosquitto_broker.h
/usr/include/mosquitto_plugin.h
/usr/include/mosquittopp.h
/usr/include/mqtt_protocol.h
/usr/lib64/libmosquitto.so
/usr/lib64/libmosquittopp.so
/usr/lib64/mosquitto_dynamic_security.so
/usr/lib64/pkgconfig/libmosquitto.pc
/usr/lib64/pkgconfig/libmosquittopp.pc
/usr/share/man/man3/libmosquitto.3

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libmosquitto.so.1
/V3/usr/lib64/libmosquittopp.so.1
/usr/lib64/libmosquitto.so.1
/usr/lib64/libmosquittopp.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mosquitto/86efdc5056a6e2e60451a6947ad69923744203b9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mosquitto_ctrl.1
/usr/share/man/man1/mosquitto_ctrl_dynsec.1
/usr/share/man/man1/mosquitto_passwd.1
/usr/share/man/man1/mosquitto_pub.1
/usr/share/man/man1/mosquitto_rr.1
/usr/share/man/man1/mosquitto_sub.1
/usr/share/man/man5/mosquitto.conf.5
/usr/share/man/man7/mosquitto-tls.7
/usr/share/man/man7/mqtt.7
/usr/share/man/man8/mosquitto.8
