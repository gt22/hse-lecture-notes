pt=src/$1
template=src/term0-template
mkdir $pt
cp -r $template/* $pt
rm $pt/core.tex $pt/switch.sh .tgconfig
ln -s $template/core.tex $pt/core.tex
ln -s $template/switch.sh $pt/switch.sh
ln -s $template/.tgconfig $pt/.tgconfig
echo "Created $1."
