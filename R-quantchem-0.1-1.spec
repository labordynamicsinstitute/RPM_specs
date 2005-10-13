########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library quantchem
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      0.1
%define packrel  1
%define rel      1
%define packname quantchem
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
Copyright: GPL
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Quantitative chemical analysis: calibration and evaluation of results
BuildRequires: R-base
PreReq: R-base
Requires:  R-outliers
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Statistical evaluation of calibration curves
by different regression techniques: ordinary, weighted,
robust (up to 4th order polynomial).
Log-log and Box-Cox transform, estimation of
optimal power and weighting scheme. Tests for heteroscedascity
and normality of residuals. Different kinds of plots
commonly used in illustrating calibrations. Easy "inverse
prediction" of concentration by given responses
and statistical evaluation of results (comparison of
precision and accuracy by common tests).

Author(s)
Lukasz Komsta

2005-09-11

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
