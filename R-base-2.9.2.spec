# spec file for R 2.9.2
# usable at least with SuSE 10.3 and 11.[01],  may be others.
# R is now part of the OpenSUSE Build Service
# D. Steuer <steuer@hsu-hh.de>

#%define _unpackaged_files_terminate_build 0

%define prefix /usr

Name: R-base
%define version 2.9.2
%define release 1 

Version: %version
Release: %release
Source: http://cran.r-project.org/src/base/R-2/R-%{version}.tar.gz
#R-%{version}.tar.bz2
#Source1: R-base-rpmlintrc
License: GPL
URL:  http://www.r-project.org/
Group: Productivity/Science/Math
Prefix: %prefix
PreReq: perl
#PreReq: , ed
Summary: R - statistics package (S-Plus like)
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: ed, gcc, gcc-c++
%if %suse_version >=1000
BuildRequires: gcc-fortran
%endif
%if %suse_version < 1000
BuildRequires: gcc-g77
%endif
BuildRequires: blas, perl
BuildRequires: libpng-devel, libjpeg-devel, readline-devel,
%if %suse_version <=1020
BuildRequires: tetex, te_latex
%endif
%if %suse_version > 1020
BuildRequires: texlive-bin-latex, texlive-bin, texlive-bin-xetex
%endif
%if %suse_version < 930
BuildRequires: XFree86-devel
Requires: XFree86-fonts-75dpi, XFree86-libs, XFree86-fonts-100dpi
%endif
%if %suse_version >= 930
BuildRequires: xorg-x11-devel
Requires: xorg-x11-fonts-75dpi, xorg-x11-libs,  xorg-x11-fonts-100dpi
%endif
BuildRequires: texinfo, tcl-devel, tk-devel
Requires: libpng, libjpeg, readline
#Requires: blas
AutoReqProv: Yes

%description

R is a language which is not entirely unlike the S language developed at
AT&T Bell Laboratories by Rick Becker, John Chambers and Allan Wilks.
AUTHORS: R Core Team

%package -n R-base-devel
Summary:					Libraries and includefiles for developing with R-base
Group:						Development/Libraries/Other
Requires:					R-base = %{version}
%description -n R-base-devel
This package provides the necessary development headers and
libraries to allow you to devel with R-base.

#debug_package

%prep 
%setup -n R-%{version}

%build -n R-%{version}
 FFLAGS="-O2" CFLAGS="-O2" CXXFLAGS="-O2" FCFLAGS="-O2" R_BROWSER="firefox" ./configure --enable-R-shlib --prefix=%{prefix}
%__make %{?jobs:-j%{jobs}}
%__make dvi
%__make pdf
#%__make info

%check
#%__make check

%install -n R-%{version}
%makeinstall
%find_lang R

%__make DESTDIR=%{buildroot} install-dvi
#%__make DESTDIR=%{buildroot} install-info
%__make DESTDIR=%{buildroot} install-pdf

chmod -x %{buildroot}%{_libdir}/R/library/mgcv/CITATION
chmod +x %{buildroot}%{_libdir}/R/share/sh/help-links.sh
chmod +x %{buildroot}%{_libdir}/R/share/sh/help-print.sh
chmod +x %{buildroot}%{_libdir}/R/share/sh/echo.sh

%__rm  %{buildroot}%{_libdir}/R/library/survival/COPYING

%__ln_s %{_libdir}/R/lib/libR.so %{buildroot}%{_libdir}/libR.so
%__ln_s %{_libdir}/R/lib/libRblas.so %{buildroot}%{_libdir}/libRblas.so
%__ln_s %{_libdir}/R/lib/libRlapack.so %{buildroot}%{_libdir}/libRlapack.so

%if %suse_version > 1020    
%fdupes -s $RPM_BUILD_ROOT  
%endif

%post
/sbin/ldconfig
%install_info --info-dir=%{_infodir} %{_infodir}/R-exts.info-1.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-FAQ.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-lang.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-admin.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-exts.info-2.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-intro.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-data.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-exts.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-ints.info.gz

%postun
/sbin/ldconfig
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-exts.info-1.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-FAQ.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-lang.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-admin.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-exts.info-2.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-intro.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-data.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-exts.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-ints.info.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files -f R.lang
%defattr(-, root, root)
%doc README
%doc %_mandir/man1/R.1*
%doc %_mandir/man1/Rscript.1*
%doc %_libdir/R/COPYING
%doc %_libdir/R/NEWS
%doc %_libdir/R/SVN-REVISION
#%doc %{_infodir}/*.gz
%doc %_libdir/R/doc/

%dir %_libdir/R


/usr/bin/*
%{_libdir}/R/bin/
%{_libdir}/R/etc/
%_libdir/R/lib/
%_libdir/R/library/
%_libdir/R/modules/
%dir %_libdir/R/share
%_libdir/R/share/encodings/
%_libdir/R/share/java/
%_libdir/R/share/locale/
%_libdir/R/share/licenses/
%_libdir/R/share/make/
%_libdir/R/share/perl/
%_libdir/R/share/R/
%_libdir/R/share/sh/
%_libdir/R/share/texmf/
%_libdir/libR*.so


%files -n R-base-devel
%defattr(-, root, root)
%_libdir/R/include/
%_libdir/pkgconfig/libR.pc

%changelog
* Tue Jun 9 2009 Detlef Steuer <steuer@hsuhh.de>
- use internal blas, so blas not required
- some additing, option for firefox