########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library snowFT
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      0.0
%define packrel  1
%define rel      1
%define packname snowFT
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
Copyright: GPL
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Fault Tolerant Simple Network of Workstations
BuildRequires: R-base
PreReq: R-base
Requires:  R-rpvm R-sn R-snow
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Extension of the snow package supporting fault tolerant and reproducible applications. It is written for the PVM communication layer.

Author(s)
Hana Sevcikova, A. J. Rossini



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
