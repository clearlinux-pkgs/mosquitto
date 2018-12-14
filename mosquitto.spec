#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x779B22DFB3E717B7 (roger@atchoo.org)
#
Name     : mosquitto
Version  : 1.5.5
Release  : 20
URL      : http://mosquitto.org/files/source/mosquitto-1.5.5.tar.gz
Source0  : http://mosquitto.org/files/source/mosquitto-1.5.5.tar.gz
Source99 : http://mosquitto.org/files/source/mosquitto-1.5.5.tar.gz.asc
Summary  : mosquitto MQTT library (C bindings)
Group    : Development/Tools
License  : EPL-1.0
Requires: mosquitto-bin = %{version}-%{release}
Requires: mosquitto-lib = %{version}-%{release}
Requires: mosquitto-license = %{version}-%{release}
Requires: mosquitto-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : openssl-dev
Patch1: 0001-Remove-ldconfig.patch

%description
Select appropriate systemd service based on your compile settings. If you
enabled WITH_SYSTEMD, use mosquitto.service.notify, otherwise use
mosquitto.service.simple. The service must be renamed to mosquitto.service
before usage. Don't forget to change default paths in service file if you
changed the default build settings.

%package bin
Summary: bin components for the mosquitto package.
Group: Binaries
Requires: mosquitto-license = %{version}-%{release}
Requires: mosquitto-man = %{version}-%{release}

%description bin
bin components for the mosquitto package.


%package dev
Summary: dev components for the mosquitto package.
Group: Development
Requires: mosquitto-lib = %{version}-%{release}
Requires: mosquitto-bin = %{version}-%{release}
Provides: mosquitto-devel = %{version}-%{release}

%description dev
dev components for the mosquitto package.


%package lib
Summary: lib components for the mosquitto package.
Group: Libraries
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
%setup -q -n mosquitto-1.5.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544814042
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1544814042
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mosquitto
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mosquitto/LICENSE.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mosquitto
/usr/bin/mosquitto_passwd
/usr/bin/mosquitto_pub
/usr/bin/mosquitto_sub

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libmosquitto.so
/usr/lib64/libmosquittopp.so
/usr/lib64/pkgconfig/libmosquitto.pc
/usr/lib64/pkgconfig/libmosquittopp.pc
/usr/share/man/man3/libmosquitto.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmosquitto.so.1
/usr/lib64/libmosquitto.so.1.5.5
/usr/lib64/libmosquittopp.so.1
/usr/lib64/libmosquittopp.so.1.5.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mosquitto/LICENSE.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mosquitto_passwd.1
/usr/share/man/man1/mosquitto_pub.1
/usr/share/man/man1/mosquitto_sub.1
/usr/share/man/man5/mosquitto.conf.5
/usr/share/man/man7/mosquitto-tls.7
/usr/share/man/man7/mqtt.7
/usr/share/man/man8/mosquitto.8
