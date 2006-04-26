Summary: Icon is a high-level, general-purpose programming language with a large repertoire of features for processing data structures and character strings. Icon is an imperative, procedural language with a syntax reminiscent of C and Pascal, but with semantics at a much higher level.
Name: icon
Version: 9.4.3
Release: 1
License: Public Domain
Prefix: /opt
Group: Languages
URL: http://www.cs.arizona.edu/icon/index.htm
Source0: icon.v943src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description

%prep
%setup -q -n icon.v943src

%build
set
make X-Configure name=linux
make
make Test

%install
install -d -m 755 %buildroot/opt/icon
install -D -m 755 bin %{buildroot}/opt/icon/bin  
install -D -m 755 lib %{buildroot}/opt/icon/lib  
# man pages
install -d -m 755 %buildroot/usr/share/man/man1
install    -m 755 man/man1/icon*.1 %buildroot/usr/share/man/man1
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc doc/


%changelog
* Tue Apr 25 2006 Lars Vilhuber <lars.vilhuber@cornell.edu> - 
- Initial build.

