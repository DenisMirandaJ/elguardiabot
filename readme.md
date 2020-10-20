# El guardia bot    
Es un bot de discord desarrollado para emular las funciones que realiza un guardia en la vida universitaria.

## Errores conocidos

## Funciones por añadir
* Que las rondas de parqueo comienzen desde las 9PM hasta las 8AM
* Que las rondas de paqueo tengan distintas frecuencias:
  * las clases tengan menor frecuencia
  * los pastos tengan mayor frecuentcia
* Comando de ayuda o información de los comandos
* Web del bot (posiblemente otro proyecto) con los comando y link al repositorio

## Comandos soportados
cada comando se utiliza con el prefijo "-" seguido de la instrucción
* `paquear`
  * El guardia realizará un paqueo grupal
* `paquear {@etiqueta}`
  * El guardia procederá a paquear a dicha persona
* `guardia rules`
  * El guardia indicará las reglas del servidor
* `guardia dar {palabra (deseablemente el sustantivo de una comida)}`
  * El guardia se comerá dicha cosa y agradecerá por ello (el es muy educado, **esperamos que usted también**)
* `guardia version!`
  * El guardia asumirá su realidad como bot y dirá su versión actual
###### _control de versiones pendiente_
Se considerará la version 1.0.0.0 como la inicial, con el guardia _estable_ siguiendo el patrón A.B.C.D donde:
- A: Identificador de gran cambio o implementación mayor.
- B: Implementaciones _normales_ o _menores_, o cambios en la funcionalidad de ellas.
- C: Correción de errores.
- D: Cambios menores.

* 1.2.0.3
  * Corregidos requerimentos

* 1.2.0.2
  * Arreglo de errores relacionados a la nueva version de constants.py

* 1.2.0.0
  * **valores.py**
    * Renombrado a **constants.py**
    * Se han redefinido los nombres de algunas constantes y se han reorganizado. Este cambio implicó una modificación en cada otro archivo que invocaba las constantes de ejecución

* 1.1.0.1
  * **requirements.txt**
    * Se corrigieron las dependencias
* 1.1.0.0
  * **valores.py**
    * Se actualizó la id del servidor de pruebas
  * **requirements.txt**
    * Se corrigieron las dependencias
  * **elguardia.py**
    * Se ha añadido el comando `-guardia help`
* 1.0.2.2
  * **irAPaquear.py**
    * Se incrementó la cantidad de clientes necesarios para el paqueo por voz
* 1.0.2.1
  * **elguardia.py**
    * Se ha deshabilitado el comando `-help` predeterminado
* 1.0.2.0
  * **elguardia.py**
    * Corregido el comando `-guardia version!`
* 1.0.1.0
  * **valores.py**
    * Corregidas rutas relativas disfuncionales de logs y sources (fixeadas a absolutas)
* 1.0.0.0
  * Primera version _estable_, capaz de paquear por etiquetas, _hablar_, generar registros de su actividad y documentado.