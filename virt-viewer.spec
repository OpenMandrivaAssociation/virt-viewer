%define	name	virt-viewer
%define	version	0.2.0
%define	release	%mkrel 2

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
BuildRequires:	xen-devel
BuildRequires:	libglade2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Virtual Machine Viewer (virt-viewer) is a lightweight interface for
interacting with the graphical display of a virtualized guest OS. It uses
GTK-VNC and libvirt to look up the VNC server details associated with the
guest. It is intended as a replacement for the traditional vncviewer
client, since the latter does not support SSL/TLS encryption of x509
certificate authentication.

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
%{_datadir}/%{name}/ui/about.glade
%{_datadir}/%{name}/ui/auth.glade
%{_datadir}/%{name}/ui/viewer.glade
