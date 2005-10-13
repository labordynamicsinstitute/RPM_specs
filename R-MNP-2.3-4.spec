########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library MNP
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      2.3
%define packrel  4
%define rel      1
%define packname MNP
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
Copyright: GPL (version 2 or later)
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - R Package for Fitting the Multinomial Probit Model
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
MNP is a publicly available R package that fits the Bayesian
multinomial probit model via Markov chain Monte Carlo. The
multinomial probit model is often used to analyze the discrete
choices made by individuals recorded in survey data. Examples where
the multinomial probit model may be useful include the analysis of
product choice by consumers in market research and the analysis of
candidate or party choice by voters in electoral studies.  The MNP
software can also fit the model with different choice sets for each
individual, and complete or partial individual choice orderings of
the available alternatives from the choice set. The estimation
is based on the efficient marginal data augmentation algorithm that
is developed by Imai and van Dyk (2005). ``A Bayesian Analysis of
the Multinomial Probit Model Using the Data Augmentation,'' Journal
of Econometrics, Vol. 124, No. 2 (February), pp. 311-334.

Author(s)
Kosuke Imai <kimai@princeton.edu>,
David A. van Dyk <dvd@uci.edu>.

2005-09-06

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
