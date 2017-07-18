#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Portable C Audio Library
Summary(pl.UTF-8):	Portable C Audio Library - przenośna biblioteka C do dźwięku
Name:		pcaudiolib
Version:	1.0
Release:	1
License:	GPL v3+
Group:		Libraries
#Source0Download: https://github.com/espeak-ng/pcaudiolib/releases
Source0:	https://github.com/espeak-ng/pcaudiolib/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	57adc57c35a3de84a7b5a4294d600d99
URL:		https://github.com/espeak-ng/pcaudiolib
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9
Requires:	pulseaudio-libs >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Portable C Audio Library (pcaudiolib) provides a C API to
different audio devices. It supports the following audio frameworks:
ALSA (Linux), OSS (POSIX), PulseAudio (Linux), QSA (QNX), XAudio2
(Windows).

%description -l pl.UTF-8
pcaudiolib (Portable C Audio Library - przenośna biblioteka C do
dźwięku) udostępnia API jęyzka C do różnych urządzeń dźwiękowych.
Obsługuje następujące szkielety (w zależności od systemu
operacyjnego): ALSA (Linux), OSS (POSIX), PulseAudio (Linux), QSA
(QNX), XAudio2 (Windows).

%package devel
Summary:	Header files for pcaudiolib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pcaudiolib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib-devel
Requires:	pulseaudio-devel >= 0.9

%description devel
Header files for pcaudiolib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki pcaudiolib.

%package static
Summary:	Static pcaudiolib library
Summary(pl.UTF-8):	Statyczna biblioteka pcaudiolib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pcaudiolib library.

%description static -l pl.UTF-8
Statyczna biblioteka pcaudiolib.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md README.md
%attr(755,root,root) %{_libdir}/libpcaudio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcaudio.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcaudio.so
%{_libdir}/libpcaudio.la
%{_includedir}/pcaudiolib

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpcaudio.a
%endif
