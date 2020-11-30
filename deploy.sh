cd frontend
npm run build
cd ..
cp "C:\Users\jjasi\Desktop\budrun\frontend\dist\static\index.html" "C:\Users\jjasi\Desktop\budrun\frontend\dist"
rm "C:\Users\jjasi\Desktop\budrun\frontend\dist\static\index.html"
python _rewrite.py