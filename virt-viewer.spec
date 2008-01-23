%define	name	virt-viewer
%define	version	0.0.2
%define	release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Virtual Machine Viewer
License:    GPLv2+
Group:      Graphical desktop/GNOME
URL:        http://virt-manager.org/
Source:     http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  libvirt-devel
BuildRequires:	libgtk-vnc-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The "Virtual Machine Manager" (virt-manager for short package name) is a
desktop application for managing virtual machines. It presents a summary view
of running domains and their live performance & resource utilization
statistics. A detailed view presents graphs showing performance & utilization
over time. Ultimately it will allow creation of new domains, and configuration
& adjustment of a domain's resource allocation & virtual hardware. Finally an
embedded VNC client viewer presents a full graphical console to the guest
domain.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/*
%{_mandir}/man1/*

