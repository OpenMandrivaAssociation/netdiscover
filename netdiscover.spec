Summary:	A network address discovering tool
Name:		netdiscover
Version:	0.3
Release:	%mkrel 0.beta7.3
License:	GPLv3
Group:		Networking/Other
URL:		http://nixgeneration.com/~jaime/netdiscover/
# http://www.pc-workshop.da.ru/cvs/netdiscover.tar.gz?view=tar
Source0:	%{name}-%{version}-beta7.tar.gz
BuildRequires:	libpcap-devel
BuildRequires:	net-devel >= 1.1.3
BuildRequires:	wget
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Netdiscover is a network address discovering tool, developed mainly for those
wireless networks without dhcp server, but it also works on hub/switched
networks. Its based on arp requests, it will send arp requests and sniff for
replies.

%prep

%setup -q -n %{name}-%{version}-beta7

%build
LC_ALL=C sh update-oui-database.sh
sh autogen.sh

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_prefix}/doc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_sbindir}/*
%{_mandir}/man8/*


%changelog
* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta7.3mdv2010.0
+ Revision: 382722
- rebuilt against libnet 1.1.3

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta7.2mdv2009.1
+ Revision: 298319
- rebuilt against libpcap-1.0.0

* Sat Sep 13 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta7.1mdv2009.0
+ Revision: 284547
- fix deps
- 0.3-beta7 (cvs snapshot) fixes #36104 (netdiscover crashes when trying to use it)
- fetch latest oui.txt file and generate needed header

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.3-0.beta6.1mdv2008.1
+ Revision: 140994
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 27 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta6.1mdv2008.0
+ Revision: 18566
- Import netdiscover



* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta5.1mdk
- netdiscover-0.3-beta6
- rebuilt against libnet1.1.2

* Thu Oct 06 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta5.1mdk
- initial Mandriva package
