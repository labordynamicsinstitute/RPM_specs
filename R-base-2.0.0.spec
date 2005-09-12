# spec file for R 2.0.0
# useable at least with SuSE 8.x,9.0,9.1 probably others.
# D. Steuer <detlef.steuer@gmx.de>

%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0

%define prefix /usr

Name: R-base
%define version 2.0.0
%define release 1 

Version: %version
Release: %release
Source: ftp://cvs.r-project.org/pub/CRAN/src/base/R-%version.tgz
Copyright: GPL
URL:  http://www.r-project.org/
Group: Applications/Math
PreReq: perl
Summary: R - statistics package (S-Plus like)
BuildRoot: /var/tmp/%{name}-root
%description

R is a language which is not entirely unlike the S language developed at
AT&T Bell Laboratories by Rick Becker, John Chambers and Allan Wilks. 
Indeed in the (present) absence of an R manual, you can (mostly) get along
by using the S manual. 

Packages have been reorganised:
Package 'base' has been split into packages 'base', 'graphics',
'stats' and 'utils'.  All four are loaded in a default
installation, but the separation allows a 'lean and mean'
version of R to be used for tasks such as building indices.
Packages ctest, eda, modreg, mva, nls, stepfun and ts have been
merged into stats, and lqs has been returned to MASS.  In all
cases a stub has been left that will issue a warning and ensure
that the appropriate new home is loaded.  All the time series
datasets have been moved to package stats.  Sweave has been
moved to utils.
Package mle has been moved to stats4 which will become the
central place for statistical S4 classes and methods
distributed with base R.  Package mle remains as a stub.

The following libs are included in base:
boot, class, cluster, datasets, foreign, graphics, grDevices, grid,
KernSmooth, lattice, MASS, methods, mgcv, nlme, nnet, rkward, rpart,
spatial, splines, stats, stats4, survival, tcltk, tools, utils

%prep 
%setup -n R-%{version}
# allow crosslinking between libraries:
#%patch -p0 -b .genlibs-patch

%build -n R-%{version}
%ifos Linux
#%ifarch i586
CXXFAGS="" CFLAGS="" FFLAGS="" ./configure --with-gnome=/opt/gnome --with-libglade-config=/opt/gnome/bin/libglade-config --enable-R-shlib --prefix=%{prefix}
#%endif
%endif

TEXINPUTS="" BIBINPUTS="" make 
TEXINPUTS="" BIBINPUTS="" make dvi
TEXINPUTS="" BIBINPUTS="" make pdf
TEXINPUTS="" BIBINPUTS="" make info
TEXINPUTS="" BIBINPUTS="" make check

%install -n R-%{version}
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%prefix/bin
mkdir -p $RPM_BUILD_ROOT%prefix/lib
mkdir -p $RPM_BUILD_ROOT%prefix/lib/R/doc
mkdir -p $RPM_BUILD_ROOT%prefix/share/info
mkdir -p $RPM_BUILD_ROOT%prefix/share/man/man1

# install info files:
cp doc/manual/*.info* $RPM_BUILD_ROOT%prefix/share/info
# Info files are installes with make install by default now.

# install pdf files:
for i in doc/manual/*.pdf; do
  cp $i $RPM_BUILD_ROOT%prefix/lib/R/doc
done

# install binary distribution:
make prefix=$RPM_BUILD_ROOT%prefix install

# remove references to build directory
mv $RPM_BUILD_ROOT%prefix/bin/R $RPM_BUILD_ROOT%prefix/bin/R.tmp
cat $RPM_BUILD_ROOT%prefix/bin/R.tmp | \
  sed -e s#$RPM_BUILD_ROOT%prefix/lib/R#%prefix/lib/R# \
  > $RPM_BUILD_ROOT%prefix/bin/R
chmod 755 $RPM_BUILD_ROOT%prefix/bin/R
mv $RPM_BUILD_ROOT%prefix/lib/R/bin/R $RPM_BUILD_ROOT%prefix/lib/R/bin/R.tmp
cat $RPM_BUILD_ROOT%prefix/lib/R/bin/R.tmp | \
  sed -e s#$RPM_BUILD_ROOT%prefix/lib/R#%prefix/lib/R# \
  > $RPM_BUILD_ROOT%prefix/lib/R/bin/R
chmod 755 $RPM_BUILD_ROOT%prefix/lib/R/bin/R
rm -f $RPM_BUILD_ROOT%prefix/lib/R/bin/R.tmp

mv $RPM_BUILD_ROOT%prefix/man/man1/R* \
   $RPM_BUILD_ROOT%prefix/share/man/man1/
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
%doc %{prefix}/share/info/*info*
%{prefix}/bin/R
%{prefix}/lib/R/COPYING
%{prefix}/lib/R/COPYING.LIB
%{prefix}/lib/R/COPYRIGHTS
%{prefix}/lib/R/FAQ
%{prefix}/lib/R/NEWS
%{prefix}/lib/R/AUTHORS
%{prefix}/lib/R/THANKS
%{prefix}/lib/R/RESOURCES
%{prefix}/lib/R/afm/
%{prefix}/lib/R/bin/
%{prefix}/lib/R/share/
%doc %{prefix}/lib/R/doc/
%{prefix}/lib/R/etc/
%{prefix}/lib/R/include/
%{prefix}/lib/R/lib/
%{prefix}/lib/R/library/
%{prefix}/lib/R/modules/
