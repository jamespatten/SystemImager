%define name     systemimager
%define ver      2.0.0
%define rel      2
%define prefix   /usr/local


Summary: Software that automates Linux installs and software distribution
Name: %name
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/System
Conflicts: systemimager-client
Source: http://download.sourceforge.net/systemimager/%{name}-%{ver}.tar.gz
BuildRoot: /tmp/%{name}-%{ver}-root
Packager: Sean Dague <japh@us.ibm.com>
Docdir: %{prefix}/doc
URL: http://systemimager.org/
Requires: rsync >= 2.4.6, syslinux >= 1.48, libappconfig-perl, dosfstools, /usr/bin/perl

%description
This is bogus and not used anywhere

%package server
Summary: Software that automates Linux installs and software distribution
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/System
Conflicts: systemimager-client
Source: http://download.sourceforge.net/systemimager/%{name}-%{ver}.tar.gz
BuildRoot: /tmp/%{name}-%{ver}-root
Packager: Sean Dague <japh@us.ibm.com>
Docdir: %{prefix}/doc
URL: http://systemimager.org/
Requires: rsync >= 2.4.6, syslinux >= 1.48, libappconfig-perl, dosfstools, /usr/bin/perl

%description server
SystemImager is software that automates Linux installs and software
distribution.  It also makes software distribution, configuration, and
operating system updates easy. You can even update from one Linux 
release version to another! SystemImager can also be used for 
content distribution on web servers.  It is most useful in environments
where you have large numbers of identical machines. Some typical
environments include: Internet server farms, high performance clusters,
computer labs, or corporate desktop environments where all workstations
have the same basic hardware configuration.

%package client
Summary: Software that automates Linux installs and software distribution
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/System
Conflicts: systemimager-server
Source: http://download.sourceforge.net/systemimager/%{name}-%{ver}.tar.gz
BuildRoot: /tmp/%{name}-%{ver}-root
Packager: Sean Dague <japh@us.ibm.com>
Docdir: %{prefix}/doc
URL: http://systemimager.org/
Requires: systemconfigurator, libappconfig-perl, rsync >= 2.4.6, /usr/bin/perl

%description client
SystemImager is software that automates Linux installs and software
distribution.  It also makes software distribution, configuration, and
operating system updates easy. You can even update from one Linux 
release version to another! SystemImager can also be used for 
content distribution on web servers.  It is most useful in environments
where you have large numbers of identical machines. Some typical
environments include: Internet server farms, high performance clusters,
computer labs, or corporate desktop environments where all workstations
have the same basic hardware configuration.

%changelog
* Sat Oct 20 2001  Sean Dague <sean@dague.net> 2.0.0-2
- Recombined client and server into one spec file

* Thu Oct 18 2001 Sean Dague <sean@dague.net> 2.0.0-1
- Initial build
- Based on work by Ken Segura <ksegura@5o7.org>

%prep
%setup

%changelog
 
%build

%install
cd $RPM_BUILD_DIR/%{name}-%{version}/
make install_server_all DESTDIR=/tmp/%{name}-%{ver}-root
make install_client_all DESTDIR=/tmp/%{name}-%{ver}-root

%clean
rm -rf $RPM_BUILD_ROOT

%post server
chkconfig --add systemimager


%postun server
chkconfig --del systemimager

%files server
%defattr(-, root, root)
%doc CHANGE.LOG COPYING CREDITS README TODO VERSION
%doc doc/manual/systemimager* doc/manual/html doc/manual/examples
%doc doc/autoinstall* doc/local.cfg
%dir /var/log/systemimager
%dir /var/lib/systemimager/images
%dir /var/lib/systemimager/scripts
%dir /usr/local/lib/systemimager
%dir /usr/local/share/systemimager/i386-boot
%dir /etc/systemimager
%config /etc/systemimager/rsyncd.conf
%config /etc/systemimager/systemimager.conf

/etc/init.d/systemimager
/var/lib/systemimager/images/*
/usr/local/sbin/addclients
/usr/local/sbin/cpimage
/usr/local/sbin/getimage
/usr/local/sbin/mkautoinstallscript
/usr/local/sbin/mkbootserver
/usr/local/sbin/mkdhcpserver
/usr/local/sbin/mkdhcpstatic
/usr/local/sbin/mvimage
/usr/local/sbin/pushupdate
/usr/local/sbin/rmimage
/usr/local/bin
/usr/local/lib/systemimager/perl/SystemImager/Common.pm
/usr/local/lib/systemimager/perl/SystemImager/Server.pm
/usr/local/share/systemimager/i386-boot/*
/usr/local/share/man/*

%files client
%defattr(-, root, root)
%doc CHANGE.LOG COPYING CREDITS README TODO VERSION afterburner 
%dir /etc/systemimager
%dir /usr/local/lib/systemimager
%config /etc/systemimager/updateclient.local.exclude

/usr/local/lib/systemimager/perl/SystemImager/Client.pm
/usr/local/sbin/updateclient
/usr/local/sbin/prepareclient

