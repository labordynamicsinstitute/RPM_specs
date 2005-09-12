########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library evir
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      1.1
%define packrel  0
%define rel      1
%define packname evir
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}.tar.gz
Copyright: GPL (Version 2 or above)
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Extreme Values in R
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Functions for extreme value theory, which may be
divided into the following groups; exploratory data analysis,
block maxima, peaks over thresholds (univariate and bivariate),
point processes, gev/gpd distributions.

Author(s)
S original (EVIS) by Alexander McNeil
<mcneil@math.ethz.ch>, R port by Alec
Stephenson <alec_stephenson@hotmail.com>.

2004-05-05

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
