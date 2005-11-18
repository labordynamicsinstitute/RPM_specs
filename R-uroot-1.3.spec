########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library uroot
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      1.3
%define packrel  0
%define rel      1
%define packname uroot
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}.tar.gz
Copyright: GPL version 2 or newer. The terms of this license are in a file called COPYING which isprovided with R
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Unit root tests and graphics for seasonal time series.
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
This package contains several methods for analysing quarterly and monthly time series.
Unit root test: ADF, KPSS, HEGY, and CH, as well as several graphics: Buys-Ballot and
seasonal cycles among others, have been implemented to accomplish either an analytical or a
graphical analysis. Combined use of both enables the user to characterize the seasonality as
deterministic, stochastic or a mixture of them.
All the applications can be run from an easy to use graphical user interface, besides, some
of the results can be exported to a LaTeX file.
Although we aim at making this interface as flexible as possible, the user must be aware of
the constraints entailed in this procedure. Omited cases could be added for particular
circumstances, modifying the source code provided in this package or consulting the
maintainer.

Author(s)
Javier L�pez-de-Lacalle <javlacalle@yahoo.es> &
Ignacio D�az-Emparanza <etpdihei@bs.ehu.es>

2005/5/15

%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0

%prep
%setup -T -c -a 0

%build
cp %{packname}/DESCRIPTION .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/R/library
%{prefix}/bin/R CMD INSTALL -l $RPM_BUILD_ROOT%{prefix}/lib/R/library %{packname}
%{prefix}/bin/R CMD check %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)


%clean
rm -rf $RPM_BUILD_ROOT

%post
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%postun
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%files
%doc DESCRIPTION
%{prefix}/lib/R/library/%{packname}


####### end of spec-file ################################################