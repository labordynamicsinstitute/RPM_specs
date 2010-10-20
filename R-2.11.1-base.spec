# spec file for R 2.9.2
# usable at least with SuSE 10.[0123]  probably others.
# R is now part of the OpenSUSE Build Service
# D. Steuer <steuer@hsu-hh.de>

%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0

%define prefix /usr

Name: R-base
%define version 2.11.1
%define release 1 

Version: %version
Release: %release
Source: http://cran.r-project.org/src/base/R-2/R-%version.tar.gz
License: GPL
URL:  http://www.r-project.org/
Group: Productivity/Science/Math
PreReq: perl, ed
Summary: R - statistics package (S-Plus like)
BuildRoot: /var/tmp/%{name}-root
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
Requires: blas
AutoReqProv: Yes

%description

R is a language which is not entirely unlike the S language developed at
AT&T Bell Laboratories by Rick Becker, John Chambers and Allan Wilks. 
Indeed in the (present) absence of an R manual, you can (mostly) get along
by using the S manual. 

%prep 
%setup -n R-%{version}
# allow crosslinking between libraries:
#%patch -p0 -b .genlibs-patch

%build -n R-%{version}
%ifos Linux
%ifarch i586
CXXFLAGS="-g -O2" CFLAGS="-g -O2" FFLAGS="-g -O2" ./configure  --enable-R-shlib --prefix=%{prefix}
%define ILD lib
%endif
%ifarch x86_64
CXXFLAGS="-g -O2" CFLAGS="-g -O2" FFLAGS="-g -O2" ./configure  --enable-R-shlib --prefix=%{prefix}
%define ILD lib64
%endif
%ifarch ia64
R_PAPERSIZE=letter CXXFLAGS="-g -O2" CFLAGS="-g -O2" FFLAGS="-g -O2" ./configure  --enable-R-shlib --prefix=%{prefix}
%define ILD lib
%endif
%endif

TEXINPUTS="" BIBINPUTS="" make 
TEXINPUTS="" BIBINPUTS="" make dvi
TEXINPUTS="" BIBINPUTS="" make pdf
#TEXINPUTS="" BIBINPUTS="" make info
TEXINPUTS="" BIBINPUTS="" make check

%install -n R-%{version}
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/%{ILD}
mkdir -p $RPM_BUILD_ROOT%prefix/%{ILD}/R/doc
mkdir -p $RPM_BUILD_ROOT%prefix/%{ILD}/R/doc/manual
mkdir -p $RPM_BUILD_ROOT%prefix/share/info
mkdir -p $RPM_BUILD_ROOT%prefix/share/man/man1

# install info files:
#cp doc/manual/*.info* $RPM_BUILD_ROOT%prefix/share/info
# Info files are installes with make install by default now.

# install pdf files:
for i in doc/manual/*.pdf; do
  cp $i $RPM_BUILD_ROOT%prefix/%{ILD}/R/doc/manual
done

# install binary distribution:
%makeinstall

#make prefix=$RPM_BUILD_ROOT%prefix install


# remove references to build directory

#mv $RPM_BUILD_ROOT%prefix/bin/R $RPM_BUILD_ROOT%prefix/bin/R.tmp
#cat $RPM_BUILD_ROOT%prefix/bin/R.tmp | \
 # sed -e s#$RPM_BUILD_ROOT%prefix/%{ILD}/R#%prefix/%{ILD}/R# \
 # > $RPM_BUILD_ROOT%prefix/bin/R
#chmod 755 $RPM_BUILD_ROOT%prefix/bin/R
#mv $RPM_BUILD_ROOT%prefix/%{ILD}/R/bin/R $RPM_BUILD_ROOT%prefix/%{ILD}/R/bin/R.tmp
#cat $RPM_BUILD_ROOT%prefix/%{ILD}/R/bin/R.tmp | \
 # sed -e s#$RPM_BUILD_ROOT%prefix/%{ILD}/R#%prefix/%{ILD}/R# \
 # > $RPM_BUILD_ROOT%prefix/%{ILD}/R/bin/R
#chmod 755 $RPM_BUILD_ROOT%prefix/%{ILD}/R/bin/R
#rm -f $RPM_BUILD_ROOT%prefix/%{ILD}/R/bin/R.tmp

#mv $RPM_BUILD_ROOT%prefix/man/man1/R* \
#   $RPM_BUILD_ROOT%prefix/share/man/man1/
# compress man pages: 
# (cd $RPM_BUILD_ROOT%prefix/share/man/man1; gzip -9f R.1 )

%post
#%_install_info R-FAQ.info

%preun
#%_remove_install_info R-FAQ.info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README
%doc %{prefix}/share/man/man1/R.1*
%doc %{prefix}/share/man/man1/Rscript.1*
#%doc %{prefix}/share/info/*info*
%{prefix}/bin/R
%{prefix}/bin/Rscript
#%{prefix}/%{ILD}/R/COPYING
#%{prefix}/%{ILD}/R/COPYING.LIB
#%{prefix}/%{ILD}/R/COPYRIGHTS
#%{prefix}/%{ILD}/R/FAQ
#%{prefix}/%{ILD}/R/NEWS
#%{prefix}/%{ILD}/R/ONEWS
#%{prefix}/%{ILD}/R/OONEWS
#%{prefix}/%{ILD}/R/AUTHORS
#%{prefix}/%{ILD}/R/THANKS
#%{prefix}/%{ILD}/R/RESOURCES
#%{prefix}/%{ILD}/R/afm/
%{prefix}/%{ILD}/pkgconfig/libR.pc
%{prefix}/%{ILD}/R/bin/
%{prefix}/%{ILD}/R/share/
%doc %{prefix}/%{ILD}/R/doc/
%{prefix}/%{ILD}/R/etc/
%{prefix}/%{ILD}/R/include/
%{prefix}/%{ILD}/R/lib/
%{prefix}/%{ILD}/R/library/
%{prefix}/%{ILD}/R/modules/
