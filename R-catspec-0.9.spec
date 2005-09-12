########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library catspec
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      0.9
%define packrel  0
%define rel      1
%define packname catspec
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}.tar.gz
Copyright: GPL version 2 or newer
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Special models for categorical variables
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
`sqtab' contains a set of functions for estimating
loglinear models for square tables such as quasi-independence,
symmetry, uniform association.
`mclgen' restructures a dataframe to enable the estimation of a
multinomial logistic model using the conditional logit program
`clogit'. This allows greater flexibility in imposing constraints on
the response variable. One application is to specify aforementioned
models for square tables as multinomial logistic models with
covariates at the respondent level.
`ctab' simplifies the production of (multiway( percentage tables.

Author(s)
John Hendrickx <John_Hendrickx@yahoo.com>



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
