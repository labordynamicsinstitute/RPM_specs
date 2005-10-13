########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library party
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      0.2
%define packrel  8
%define rel      1
%define packname party
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
Copyright: GPL
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - A Laboratory for Recursive Part(y)itioning
BuildRequires: R-base
PreReq: R-base
Requires:  R-coin R-modeltools
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Unbiased recursive partitioning in a conditional
inference framework. This package implements a unified
framework for recursive partitioning which embeds tree-structured
regression models into a well defined theory of conditional inference
procedures. Stopping criteria based on multiple test procedures
are implemented. The methodology is applicable to all kinds of
regression problems, including nominal, ordinal, numeric, censored
as well as multivariate response variables and arbitrary measurement
scales of the covariates. Extensible functionality for visualizing
tree-structured regression models is available.

Author(s)
Torsten Hothorn, Kurt Hornik and Achim Zeileis

$Date: 2005/09/06 15:52:10 $

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
