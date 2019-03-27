%define _disable_rebuild_configure 1

Name:		virt-viewer
Version:	8.0
Release:	1
Summary:	Virtual Machine Viewer
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://virt-manager.org/
Source0:	http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
BuildRequires: pkgconfig(glib-2.0) >= 2.22.0
BuildRequires: pkgconfig(gmodule-export-2.0)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.0
BuildRequires: pkgconfig(gtk-vnc-2.0) >= 0.4.0
BuildRequires: pkgconfig(libvirt)
BuildRequires: pkgconfig(libvirt-glib-1.0)
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires: pkgconfig(spice-client-gtk-3.0) >= 0.12.101
BuildRequires: pkgconfig(spice-protocol) >= 0.10.1
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:  pkgconfig(shared-mime-info)

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
%configure --with-gtk=3.0 --disable-update-mimedb
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README.md
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/mime/packages/virt-viewer-mime.xml
%{_datadir}/applications/remote-viewer.desktop
%{_datadir}/appdata/remote-viewer.appdata.xml
%{_datadir}/icons/hicolor/*/*
