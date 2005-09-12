########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library seqmon
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      0.1
%define packrel  0
%define rel      1
%define packname seqmon
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}.tar.gz
Copyright: GPL
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Sequential Monitoring of Clinical Trials
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
A program that computes the probability of crossing sequential boundaries in a
clinical trial. It implements the Armitage-McPherson and Rowe Algorithm using the method
described in Schoenfeld D. (2001)" A simple Algorithm for Designing Group Sequential Clinical
Trials" Biometrics 27: pp, 972-974

Author(s)
David A. Schoenfeld <dschoenfeld@partners.org>

2004-05-30

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
