if [ -e conspect.tex.latexmain ]
then
    rm conspect.tex.latexmain
    touch conspect_lectures.tex.latexmain
    echo "Switching to lectures"
else
    rm conspect_lectures.tex.latexmain
    touch conspect.tex.latexmain
    echo "Switching to normal"
fi
