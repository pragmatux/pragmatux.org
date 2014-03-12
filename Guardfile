# Guardfile
# More info at https://github.com/guard/guard#readme

guard 'shell' do
  watch(/(.*).asciidoc$/) {|m| `./_make.sh` }
  watch(/(.*).md$/) {|m| `./_make.sh` }
  watch(/(.*).html_$/) {|m| `./_make.sh` }
end

guard 'livereload' do
  watch(/(.*).html$/)
end
