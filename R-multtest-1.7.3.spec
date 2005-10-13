########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library multtest
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      1.7.3
%define packrel  0
%define rel      1
%define packname multtest
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}.tar.gz
Copyright: LGPL
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Resampling-based multiple hypothesis testing
BuildRequires: R-base
PreReq: R-base
Requires: 
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Non-parametric bootstrap and permutation resampling-based multiple testing procedures for controlling the family-wise error rate (FWER), generalized family-wise error rate (gFWER), tail probability of the proportion of false positives (TPPFP), and false discovery rate (FDR). Single-step and step-wise methods are implemented. Tests based on a variety of t- and F-statistics (including t-statistics based on regression parameters from linear and survival models) are included. Results are reported in terms of adjusted p-values, confindence regions and test statistic cutoffs.

Author(s)
Katherine S. Pollard, Yongchao Ge, Sandrine Dudoit



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
