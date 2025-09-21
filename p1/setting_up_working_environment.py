# Bilgisayaramızdaki sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create -n virtual_environment_name

# Sanal ortamı aktif etme:
# conda activate virtual_environment_name

# Sanal ortamı deactivate etme:
# conda deactivate virtual_environment_name

# Sanal ortam içerisindeki paketleri görüntüleme
# conda list

# sanal ortama paket yükleme:
# conda install package_name

# birden fazla paketi aynı anda yüklemek için:
# conda install package_name1 package_name2 package_name3 ...

# paket silme:
# conda remove package_name

# belirli bir versiyona göre paket yükleme:
# conda install package_name=1.20.1

# paket yükseltme
# conda upgrade package_name

# tüm paketlerin yükseltşilmesi:
# conda upgrade -all

# environment file oluşturma:
# conda env export > environment.yaml

# oluşturulan sanal ortamı silmek için:
# conda env remove -n virtual_environment_name

# environment dosyasından sanal ortam oluşturmak: (environment.yaml dosya adı)
# conda env create -f environment.yaml

#------------ Pip kullanarak paket işlemlerinin yapılması:
# paket yükleme:
# pip install package_name

# paket yükleme verisiyona göre:
# pip install package_name==1.20.1

