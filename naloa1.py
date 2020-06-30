# 1. naloga
def izracuna_vsoto_vseh_naravnih_stevil_pod_stevilom_ki_so_deljiva_bodisi_s_pet_bodisi_s_tri(m):
    vsota = 0
    for i in range(m):                               
        if i % 3 == 0 or i % 5 == 0:
            vsota += i
    return vsota 
print(izracuna_vsoto_vseh_naravnih_stevil_pod_stevilom_ki_so_deljiva_bodisi_s_pet_bodisi_s_tri(1000))
233168