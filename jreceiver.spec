Summary: JReceiver 
Name: JReceiver
Version: 0.2.5
Release: 1
License: modified BSD
Group: Server
URL: http://jreceiver.sourceforge.net/
Source0: %{name}-%{version}.tgz
Source1: %{name}-extras.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: JReceiver-Jetty >= 4.2 java mysql-client
#Requires: java >1.3  
#Requires: mysql-client

%description
JReceiver is a servlet-based audio server which features tightly integrated metadata indexing capabilities, browser-based management, an XML-RPC interface and support for network-based MP3 players like the Rio Receiver from Sonic Blue.

After installation, configure the server as per http://jreceiver.sourceforge.net/jrec-install-server.html. The server will then be available at http://HOSTNAME:8080/jreceiver

%prep
# %setup -q
%build

%install
set
rm -rf $RPM_BUILD_ROOT
install -o root -d -m 755 %buildroot/usr/local/
cd %buildroot/usr/local
tar xzvf %{SOURCE0}
ln -s %{name}-%{version} jreceiver
# install the init.d module
# untars to /etc/init.d
cd %buildroot
tar xzvf %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
#%doc
/usr/local/JReceiver-0.2.5/bin/jrec_jetty.bat
/usr/local/JReceiver-0.2.5/bin/admin.password
/usr/local/JReceiver-0.2.5/bin/jrec_jetty.sh
/usr/local/JReceiver-0.2.5/dist/jrec_mgr.war
/usr/local/JReceiver-0.2.5/dist/jrec_rio.war
/usr/local/JReceiver-0.2.5/dist/jrec_serv.war
/usr/local/JReceiver-0.2.5/doc/rio/index.html
/usr/local/JReceiver-0.2.5/doc/rio/jrec-faq-rio.html
/usr/local/JReceiver-0.2.5/doc/rio/jrec-install-rio.html
/usr/local/JReceiver-0.2.5/doc/rio/jrec-trouble-rio.html
/usr/local/JReceiver-0.2.5/doc/rio/rioarch.png
/usr/local/JReceiver-0.2.5/doc/arch.png
/usr/local/JReceiver-0.2.5/doc/banner.png
/usr/local/JReceiver-0.2.5/doc/desktop.png
/usr/local/JReceiver-0.2.5/doc/email.gif
/usr/local/JReceiver-0.2.5/doc/homebuilt.png
/usr/local/JReceiver-0.2.5/doc/index.css
/usr/local/JReceiver-0.2.5/doc/index.html
/usr/local/JReceiver-0.2.5/doc/jrec-faq.html
/usr/local/JReceiver-0.2.5/doc/jrec-install-java.html
/usr/local/JReceiver-0.2.5/doc/jrec-install-jetty.html
/usr/local/JReceiver-0.2.5/doc/jrec-install-mysql.html
/usr/local/JReceiver-0.2.5/doc/jrec-install-server.html
/usr/local/JReceiver-0.2.5/doc/jrec-install.html
/usr/local/JReceiver-0.2.5/doc/jrec-trouble.html
/usr/local/JReceiver-0.2.5/doc/redrat2.png
/usr/local/JReceiver-0.2.5/doc/rio.png
/usr/local/JReceiver-0.2.5/doc/smallelf.png
/usr/local/JReceiver-0.2.5/doc/tarch.png
/usr/local/JReceiver-0.2.5/doc/tdesktop.png
/usr/local/JReceiver-0.2.5/doc/tux.png
/usr/local/JReceiver-0.2.5/doc/winlogo.png
/usr/local/JReceiver-0.2.5/etc/commons-logging.properties
/usr/local/JReceiver-0.2.5/etc/jrec_jetty.xml
/usr/local/JReceiver-0.2.5/etc/jrec_mysql.sql
/usr/local/JReceiver-0.2.5/etc/log4j.properties
/usr/local/JReceiver-0.2.5/etc/simplelog.properties
/usr/local/JReceiver-0.2.5/etc/tag_policy.xslt
/usr/local/JReceiver-0.2.5/etc/jreceiver.properties
/usr/local/JReceiver-0.2.5/CHANGES.txt
/usr/local/JReceiver-0.2.5/INSTALL.txt
/usr/local/JReceiver-0.2.5/LICENSE.txt
/usr/local/JReceiver-0.2.5/logs/
/etc/init.d/jreceiver


%changelog
* Sun Apr  2 2006 Lars Vilhuber <vilhuber@belanger.cloutier-vilhuber.net> - 
- Initial build.

