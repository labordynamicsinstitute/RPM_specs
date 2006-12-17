########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library network
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      1.1
%define packrel  1
%define rel      1
%define packname network
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
Copyright: GPL version 2 (June, 1991)
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Classes for Relational Data
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Tools to create and modify network objects.  The network class can represent a range of relational data types, and supports arbitrary vertex/edge/graph attributes.

Author(s)
Carter T. Butts <buttsc@uci.edu>, with help
from David Hunter <dhunter@stat.psu.edu>
and Mark S. Handcock <handcock@stat.washington.edu>

October 10, 2006

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
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --html
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%postun
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --html
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%files
%doc DESCRIPTION
%{prefix}/lib/R/library/%{packname}


####### end of spec-file ################################################
