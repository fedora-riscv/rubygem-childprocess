%global gem_name childprocess

%global rubyabi 1.9.1

Summary: A simple and reliable gem for controlling external programs
Name: rubygem-%{gem_name}
Version: 0.2.0
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/jarib/childprocess
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
Requires: rubygem(ffi) => 1.0.6
Requires: rubygem(ffi) < 1.1
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec-core)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_instdir}/.document %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.rspec %{buildroot}%{gem_instdir}/Rakefile
rm -f %{buildroot}%{gem_instdir}/childprocess.gemspec
rm -f %{buildroot}%{gem_instdir}/Gemfile
chmod 644 %{buildroot}%{gem_libdir}/childprocess/jruby/process.rb
chmod 644 %{buildroot}%{gem_libdir}/childprocess/windows/process.rb
chmod 644 %{buildroot}%{gem_instdir}/spec/*.rb

%check
pushd .%{gem_instdir}
rspec spec
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/spec


%changelog
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.2.0-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 03 2011 Chris Lalancette <clalance@redhat.com> - 0.2.0-1
- Initial package
