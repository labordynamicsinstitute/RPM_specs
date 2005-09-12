########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library Design
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      2.0
%define packrel  9
%define rel      1
%define packname Design
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
Copyright: GPL version 2 or newer
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Design Package
BuildRequires: R-base
PreReq: R-base
Requires:  R-Hmisc
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Regression modeling, testing, estimation, validation,
graphics, prediction, and typesetting by storing enhanced model design
attributes in the fit.  Design is a collection of about 180 functions
that assist and streamline modeling, especially for biostatistical and
epidemiologic applications.  It also contains new functions for binary
and ordinal logistic regression models and the Buckley-James multiple
regression model for right-censored responses, and implements
penalized maximum likelihood estimation for logistic and ordinary
linear models.  Design works with almost any regression model, but it
was especially written to work with logistic regression, Cox
regression, accelerated failure time models, ordinary linear models,
the Buckley-James model, and generalized least squares for
serially or spatially correlated observations.

Author(s)
Frank E Harrell Jr <f.harrell@vanderbilt.edu>

2004-09-05

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
