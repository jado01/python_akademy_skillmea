# Príklad – Kruhová kontrola
# Máš polomer kruhu r.
# Vypočítaj:
# obvod: O=2πr
# obsah: S=πr2
# priemer: d=2r
# Skontroluj logicky:
# Je obvod väčší ako 40?
# Je obsah menší ako 200?
# Výsledky vypíš s dvoma desatinnými miestami, spolu s hodnotou True/False pre obe podmienky.

import math

r = 4
obvod = 2 * math.pi * r
obsah = math.pi * r**2
priemer = 2 * r

print(f"Obvod kruhu je: {obvod:.2f} (väčší ako 40? {obvod > 40})")
print(f"Obsah kruhu je: {obsah:.2f} (mensi ako 200? {obsah < 200})")
print(f"Priemer kruhu je: {priemer:.2f}")
