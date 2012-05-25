%define	name	virt-viewer
%define	version	0.5.3
%define	release	1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Virtual Machine Viewer
License:    GPLv2+
Group:      Graphical desktop/GNOME
URL:        http://virt-manager.org/
Source:     http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  libvirt-devel
BuildRequires:	gtk-vnc-devel
BuildRequires:	xen-devel
BuildRequires:	intltool
BuildRequires:	pkgconfig(libglade-2.0)

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
%makeinstall_std
%find_lang %{name}

%clean


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/remote-viewer.desktop
%{_datadir}/icons/hicolor/*/*
%{_datadir}/%{name}/ui
