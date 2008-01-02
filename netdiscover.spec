Summary:	A network address discovering tool
Name:		netdiscover
Version:	0.3
Release:	%mkrel 0.beta6.1
License:	GPL
Group:		Networking/Other
URL:		http://nixgeneration.com/~jaime/netdiscover/
Source0:	http://nixgeneration.com/~jaime/netdiscover/releases/%{name}-%{version}-beta6.tar.bz2
BuildRequires:	libpcap-devel
BuildRequires:	libnet1.1.2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Netdiscover is a network address discovering tool, developed
mainly for those wireless networks without dhcp server, but it
also works on hub/switched networks. Its based on arp requests, it
will send arp requests and sniff for replies.

%prep

%setup -q -n %{name}-%{version}-beta6

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -rf %{buildroot}%{_prefix}/doc

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_sbindir}/*
%{_mandir}/man8/*
