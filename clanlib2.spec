%define origname clanlib
%define api 2.2
%define libmajor 1
%define libname %mklibname %{origname} %{api} %{libmajor}
%define develname %mklibname -d %{origname} %{api}

Name:		%{origname}2
Summary:	The ClanLib Game SDK
Version:	2.2.12
Release:	2
License:	BSD-like
Group:		System/Libraries
Source0:	http://www.clanlib.org/download/releases-2.0/ClanLib-%version.tgz
Patch0:		ClanLib-2.2.9-link.patch
URL:		http://www.clanlib.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	GL-devel
BuildRequires:	libx11-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype2-devel
BuildRequires:	jpeg-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	pcre-devel
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel

%description
The ClanLib Game SDK is a crossplatform game library designed to ease the work
for game developers. The goal is to provide a common interface to classical
game problems (loading graphics eg.), so games can share as much code as
possible. Ideally anyone with small resources should be able to write
commercial quality games.

%package -n	%{libname}
Summary:	Main library for %{origname}
Group:		System/Libraries
Provides:	%{origname} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Provides:	%{origname}%{api} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{origname}.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{origname}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{origname}-devel = %{version}-%{release}
Provides:	%{origname}%{api}-devel  = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{origname}.

%prep
%setup -q -n ClanLib-%{version}
%patch0 -p0 -b .link

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc README COPYING CREDITS
%{_libdir}/libclan*-%{api}.so.%{libmajor}
%{_libdir}/libclan*-%{api}.so.%{libmajor}.*

%files -n %{develname}
%defattr(-, root, root)
%doc README COPYING CODING_STYLE ascii-logo
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
