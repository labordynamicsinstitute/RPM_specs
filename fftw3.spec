#
# spec file for package fftw3 (Version 3.1.2)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           fftw3
BuildRequires:  gcc-g77 pkgconfig
Summary:        Discrete Fourier Transform (DFT) C Subroutine Library
Version:        3.1.2
Release:        32.1
License:        GNU General Public License (GPL)
Group:          Productivity/Scientific/Math
Source:         fftw-%{version}.tar.bz2
Patch:          fftw-%{version}.diff
URL:            http://www.fftw.org
Autoreqprov:    on
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         %install_info_prereq

%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.



Authors:
--------
    Matteo Frigo <athena@fftw.org>
    Stevenj G. Johnson <stevenj@alum.mit.edu>

%package devel
Summary:        Include Files and Libraries mandatory for Development.
Group:          Productivity/Scientific/Math
Requires:       fftw3 = %{version}-%{release} glibc-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.



Authors:
--------
    Matteo Frigo <athena@fftw.org>
    Stevenj G. Johnson <stevenj@alum.mit.edu>

%package threads
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Productivity/Scientific/Math
Requires:       fftw3 = %{version}-%{release}

%description threads
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.



Authors:
--------
    Matteo Frigo <athena@fftw.org>
    Stevenj G. Johnson <stevenj@alum.mit.edu>

%package threads-devel
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Productivity/Scientific/Math
Requires:       fftw3-threads = %{version}-%{release}
Requires:       fftw3-devel = %{version}-%{release} glibc-devel

%description threads-devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.



Authors:
--------
    Matteo Frigo <athena@fftw.org>
    Stevenj G. Johnson <stevenj@alum.mit.edu>

%prep
%setup -q -n fftw-%{version}
%patch
%{?suse_update_config:%{suse_update_config -f }}
autoreconf --force --install

%build
%configure --enable-shared --enable-threads --disable-static
make %{?jobs:-j %jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT install
# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.*a
# hack to also compile/install single-precision version:
make distclean
%configure --enable-shared --enable-threads --enable-float --disable-static
make %{?jobs:-j %jobs}
make DESTDIR=$RPM_BUILD_ROOT install
# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.*a
# gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/fftw3.info.gz

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/fftw3.info.gz

%post
%run_ldconfig

%postun
%run_ldconfig

%post threads
%run_ldconfig

%postun threads
%run_ldconfig

%clean
test "$RPM_BUILD_ROOT" != "/" -a -d "$RPM_BUILD_ROOT" && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/libfftw3.so.*
%{_libdir}/libfftw3f.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS CONVENTIONS COPYING COPYRIGHT ChangeLog INSTALL NEWS README TODO
%doc doc/*
%doc %{_mandir}/man?/*
%{_infodir}/*.info*
%{_includedir}/*
%{_libdir}/libfftw3.so
%{_libdir}/libfftw3f.so
%{_libdir}/pkgconfig/*.pc
%{_bindir}/*

%files threads
%defattr(-,root,root)
%{_libdir}/libfftw3_threads.so.*
%{_libdir}/libfftw3f_threads.so.*

%files threads-devel
%defattr(-,root,root)
%{_libdir}/libfftw3_threads.so
%{_libdir}/libfftw3f_threads.so

%changelog
* Mon Apr 16 2007 tiwai@suse.de
- follow library packaging policy
  * move docs to devel package
  * remove static libraries
* Sat Oct 21 2006 schwab@suse.de
- Fix broken macro.
* Tue Aug 22 2006 tiwai@suse.de
- updated to version 3.1.2:
  * correct bug in configure script
  * updated FAQ
  * use -maltivec when checking for altivec.h.
- clean up spec file, using %%configure macro.
* Thu May 18 2006 tiwai@suse.de
- major update to version 3.1.1:
  * fixed texi files
  * lots of configure fixes
  * clean up and optimizations
  see ChangeLog for details
- added missing glibc-devel to Requires of devel subpackages
- removed -fno-strict-aliasing option
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Apr 13 2005 tiwai@suse.de
- fixed neededforbuild.
* Tue Apr 27 2004 ro@suse.de
- add -fno-strict-aliasing
* Sat Jan 10 2004 adrian@suse.de
- add missing %%defattr and %%run_ldconfig
* Fri Aug 29 2003 nashif@suse.de
- #29586: info file installation in wrong post segment
* Wed Jul 30 2003 nashif@suse.de
- Initial release
