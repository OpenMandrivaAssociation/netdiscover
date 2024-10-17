Summary:	A network address discovering tool
Name:		netdiscover
Version:	0.3
Release:	0.beta7.5
License:	GPLv3+
Group:		Networking/Other
Url:		https://nixgeneration.com/~jaime/netdiscover/
# http://www.pc-workshop.da.ru/cvs/netdiscover.tar.gz?view=tar
Source0:	%{name}-%{version}-beta7.tar.gz
BuildRequires:	libtool
BuildRequires:	wget
BuildRequires:	libnet-devel >= 1.1.3
BuildRequires:	pcap-devel

%description
Netdiscover is a network address discovering tool, developed mainly for those
wireless networks without dhcp server, but it also works on hub/switched
networks. Its based on arp requests, it will send arp requests and sniff for
replies.

%files
%doc AUTHORS ChangeLog README TODO
%{_sbindir}/*
%{_mandir}/man8/*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-beta7
find . -name "Makefile*" -o -name "*.m4" -o -name "configure*" |xargs sed -i -e 's,configure.in,configure.ac,g'

find . -perm 640 | xargs chmod 0644

%build
LC_ALL=C sh update-oui-database.sh
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_prefix}/doc

