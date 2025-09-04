
"""
Librería de utilidades en español para Programación 1.
Incluye:
- Colores (colorama con fallback)
- Entradas robustas con bucles infinitos y opción CANCELAR
- Validaciones (email, CUIT/CUIL, rangos numéricos)
- Lectura básica de .txt
"""

from typing import Optional, Iterable, Tuple, List, Dict
import re

# --- Colorama (con fallback si no está instalada) ---
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    _OK = Fore.GREEN + Style.BRIGHT
    _ERR = Fore.RED + Style.BRIGHT
    _WARN = Fore.YELLOW + Style.BRIGHT
    _INFO = Fore.CYAN + Style.BRIGHT
    _TITLE = Fore.MAGENTA + Style.BRIGHT
    _RESET = Style.RESET_ALL
except Exception:
    class _Dummy:
        def __getattr__(self, _): return ""
    Fore = Style = _Dummy()
    _OK = _ERR = _WARN = _INFO = _TITLE = _RESET = ""

# --- Excepción para cancelar el flujo ---
class FlujoCancelado(Exception):
    pass

# --- Helpers de impresión con estilo ---
def titulo(msg: str): print(f"{_TITLE}{msg}{_RESET}")
def ok(msg: str):     print(f"{_OK}✔ {msg}{_RESET}")
def error(msg: str):  print(f"{_ERR}✖ {msg}{_RESET}")
def warn(msg: str):   print(f"{_WARN}⚠ {msg}{_RESET}")
def info(msg: str):   print(f"{_INFO}ℹ {msg}{_RESET}")

# --- Entrada robusta con CANCELAR ---
def _leer_input(prompt: str, cancelar: str = "CANCELAR") -> str:
    dato = input(prompt).strip()
    if dato.upper() == cancelar.upper():
        raise FlujoCancelado("El usuario canceló el flujo.")
    return dato

def pedir_texto(prompt: str, permitir_vacio: bool = False,
                cancelar: str = "CANCELAR") -> str:
    """Pide texto en bucle hasta que sea válido o el usuario cancele."""
    while True:
        try:
            dato = _leer_input(prompt, cancelar)
            if dato == "" and not permitir_vacio:
                error("No puede estar vacío. Escriba algo o 'CANCELAR'.")
                continue
            return dato
        except FlujoCancelado:
            raise

def pedir_opcion(prompt: str, opciones: Iterable[str],
                 cancelar: str = "CANCELAR") -> str:
    """Pide una opción (case-insensitive). Muestra opciones válidas."""
    opciones_norm = [o.strip() for o in opciones]
    opciones_low = [o.lower() for o in opciones_norm]
    while True:
        try:
            info(f"Opciones válidas: {', '.join(opciones_norm)}")
            dato = _leer_input(prompt, cancelar)
            if dato.lower() in opciones_low:
                # Devuelve con la forma original (no lower)
                return opciones_norm[opciones_low.index(dato.lower())]
            error("Opción inválida. Intente nuevamente o 'CANCELAR'.")
        except FlujoCancelado:
            raise

def pedir_entero(prompt: str, minimo: Optional[int] = None,
                 maximo: Optional[int] = None, cancelar: str = "CANCELAR") -> int:
    while True:
        try:
            dato = _leer_input(prompt, cancelar)
            try:
                n = int(dato)
            except ValueError:
                error("Debe ser un número entero.")
                continue
            if minimo is not None and n < minimo:
                error(f"Debe ser ≥ {minimo}.")
                continue
            if maximo is not None and n > maximo:
                error(f"Debe ser ≤ {maximo}.")
                continue
            return n
        except FlujoCancelado:
            raise

def pedir_float(prompt: str, minimo: Optional[float] = None,
                maximo: Optional[float] = None, cancelar: str = "CANCELAR") -> float:
    while True:
        try:
            dato = _leer_input(prompt, cancelar)
            try:
                x = float(dato.replace(",", "."))  # permitir coma
            except ValueError:
                error("Debe ser un número (use . o , para decimales).")
                continue
            if minimo is not None and x < minimo:
                error(f"Debe ser ≥ {minimo}.")
                continue
            if maximo is not None and x > maximo:
                error(f"Debe ser ≤ {maximo}.")
                continue
            return x
        except FlujoCancelado:
            raise

def confirmar(prompt: str = "¿Confirmar? (s/n) ", cancelar: str = "CANCELAR") -> bool:
    while True:
        try:
            dato = _leer_input(prompt, cancelar)
            if dato.lower() in ("s", "si", "sí"):
                return True
            if dato.lower() in ("n", "no"):
                return False
            warn("Responda 's' o 'n' (o 'CANCELAR').")
        except FlujoCancelado:
            raise

# --- Validaciones ---

_email_re = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def validar_email(s: str) -> bool:
    return bool(_email_re.match(s.strip()))

def normalizar_cuit(cuit: str) -> Optional[str]:
    """Devuelve 11 dígitos o None. Acepta formatos con guiones/espacios."""
    digitos = re.sub(r"\D", "", cuit)
    return digitos if len(digitos) == 11 else None

def _dv_cuit(diez_digitos: str) -> int:
    """Calcula dígito verificador CUIT/CUIL (método AFIP)."""
    pesos = [5,4,3,2,7,6,5,4,3,2]
    s = sum(int(d)*p for d, p in zip(diez_digitos, pesos))
    mod = s % 11
    dv = 11 - mod
    if dv == 11: return 0
    if dv == 10: return 9
    return dv

def validar_cuit(cuit: str) -> bool:
    norm = normalizar_cuit(cuit)
    if not norm:
        return False
    base, dv = norm[:10], int(norm[10])
    return _dv_cuit(base) == dv

def pedir_email(prompt: str = "Email: ", cancelar: str = "CANCELAR") -> str:
    while True:
        try:
            s = _leer_input(prompt, cancelar)
            if validar_email(s):
                return s
            error("Email inválido. Ej: nombre@dominio.com")
        except FlujoCancelado:
            raise

def pedir_cuit(prompt: str = "CUIT/CUIL (ej 20-12345678-9): ", cancelar: str = "CANCELAR") -> str:
    while True:
        try:
            s = _leer_input(prompt, cancelar)
            if validar_cuit(s):
                return s
            error("CUIT/CUIL inválido. Formato y dígito verificador incorrectos.")
        except FlujoCancelado:
            raise

# --- Lectura simple de .txt ---
def leer_lineas_txt(ruta: str, strip: bool = True) -> List[str]:
    with open(ruta, "r", encoding="utf-8") as f:
        if strip:
            return [ln.strip() for ln in f.readlines()]
        return list(f.readlines())

def filtrar_enteros_validos(lineas: Iterable[str],
                            minimo: Optional[int] = None,
                            maximo: Optional[int] = None) -> Tuple[List[int], List[str]]:
    """Devuelve (validos, rechazados_str)."""
    validos, rechazados = [], []
    for ln in lineas:
        try:
            n = int(ln)
            if (minimo is not None and n < minimo) or (maximo is not None and n > maximo):
                rechazados.append(ln)
            else:
                validos.append(n)
        except ValueError:
            rechazados.append(ln)
    return validos, rechazados
