Summary:	A network address discovering tool
Name:		netdiscover
Version:	0.3
Release:	%mkrel 0.beta7.1
License:	GPLv3
Group:		Networking/Other
URL:		http://nixgeneration.com/~jaime/netdiscover/
# http://www.pc-workshop.da.ru/cvs/netdiscover.tar.gz?view=tar
Source0:	%{name}-%{version}-beta7.tar.gz
BuildRequires:	libpcap-devel
BuildRequires:	libnet1.1.2-devel
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
