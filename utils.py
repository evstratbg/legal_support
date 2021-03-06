from model import Aliases, fn
import logging
import functools

def get_alias_match(message):
    check_aliases = (Aliases.select().where((fn.lower(Aliases.alias1) == message) |
                                                (fn.lower(Aliases.alias2) == message) |
                                                (fn.lower(Aliases.alias3) == message) |
                                                (fn.lower(Aliases.alias4) == message) |
                                                (fn.lower(Aliases.alias5) == message) |
                                                (fn.lower(Aliases.alias6) == message) |
                                                (fn.lower(Aliases.alias7) == message) |
                                                (fn.lower(Aliases.alias8) == message) |
                                                (fn.lower(Aliases.alias9) == message) |
                                                (fn.lower(Aliases.alias10) == message) |
                                                (fn.lower(Aliases.alias11) == message) |
                                                (fn.lower(Aliases.alias12) == message) |
                                                (fn.lower(Aliases.alias13) == message) |
                                                (fn.lower(Aliases.alias14) == message) |
                                                (fn.lower(Aliases.alias15) == message) |
                                                (fn.lower(Aliases.alias16) == message) |
                                                (fn.lower(Aliases.alias17) == message) |
                                                (fn.lower(Aliases.alias18) == message) |
                                                (fn.lower(Aliases.alias19) == message) |
                                                (fn.lower(Aliases.alias20) == message) |
                                                (fn.lower(Aliases.alias21) == message) |
                                                (fn.lower(Aliases.alias22) == message) |
                                                (fn.lower(Aliases.alias23) == message) |
                                                (fn.lower(Aliases.alias24) == message) |
                                                (fn.lower(Aliases.alias25) == message) |
                                                (fn.lower(Aliases.alias26) == message) |
                                                (fn.lower(Aliases.alias27) == message) |
                                                (fn.lower(Aliases.alias28) == message) |
                                                (fn.lower(Aliases.alias29) == message) |
                                                (fn.lower(Aliases.alias30) == message) |
                                                (fn.lower(Aliases.alias31) == message) |
                                                (fn.lower(Aliases.alias32) == message) |
                                                (fn.lower(Aliases.alias33) == message) |
                                                (fn.lower(Aliases.alias34) == message) |
                                                (fn.lower(Aliases.alias35) == message) |
                                                (fn.lower(Aliases.alias36) == message) |
                                                (fn.lower(Aliases.alias37) == message) |
                                                (fn.lower(Aliases.alias38) == message) |
                                                (fn.lower(Aliases.alias39) == message) |
                                                (fn.lower(Aliases.alias40) == message) |
                                                (fn.lower(Aliases.alias41) == message) |
                                                (fn.lower(Aliases.alias42) == message) |
                                                (fn.lower(Aliases.alias43) == message) |
                                                (fn.lower(Aliases.alias44) == message) |
                                                (fn.lower(Aliases.alias45) == message) |
                                                (fn.lower(Aliases.alias46) == message) |
                                                (fn.lower(Aliases.alias47) == message) |
                                                (fn.lower(Aliases.alias48) == message) |
                                                (fn.lower(Aliases.alias49) == message) |
                                                (fn.lower(Aliases.alias50) == message) |
                                                (fn.lower(Aliases.alias51) == message) |
                                                (fn.lower(Aliases.alias52) == message) |
                                                (fn.lower(Aliases.alias53) == message) |
                                                (fn.lower(Aliases.alias54) == message) |
                                                (fn.lower(Aliases.alias55) == message) |
                                                (fn.lower(Aliases.alias56) == message) |
                                                (fn.lower(Aliases.alias57) == message) |
                                                (fn.lower(Aliases.alias58) == message) |
                                                (fn.lower(Aliases.alias59) == message) |
                                                (fn.lower(Aliases.alias60) == message) |
                                                (fn.lower(Aliases.alias61) == message) |
                                                (fn.lower(Aliases.alias62) == message) |
                                                (fn.lower(Aliases.alias63) == message) |
                                                (fn.lower(Aliases.alias64) == message) |
                                                (fn.lower(Aliases.alias65) == message) |
                                                (fn.lower(Aliases.alias66) == message) |
                                                (fn.lower(Aliases.alias67) == message) |
                                                (fn.lower(Aliases.alias68) == message) |
                                                (fn.lower(Aliases.alias69) == message) |
                                                (fn.lower(Aliases.alias70) == message) |
                                                (fn.lower(Aliases.alias71) == message) |
                                                (fn.lower(Aliases.alias72) == message) |
                                                (fn.lower(Aliases.alias73) == message) |
                                                (fn.lower(Aliases.alias74) == message) |
                                                (fn.lower(Aliases.alias75) == message) |
                                                (fn.lower(Aliases.alias76) == message) |
                                                (fn.lower(Aliases.alias77) == message) |
                                                (fn.lower(Aliases.alias78) == message) |
                                                (fn.lower(Aliases.alias79) == message) |
                                                (fn.lower(Aliases.alias80) == message) |
                                                (fn.lower(Aliases.alias81) == message) |
                                                (fn.lower(Aliases.alias82) == message) |
                                                (fn.lower(Aliases.alias83) == message) |
                                                (fn.lower(Aliases.alias84) == message) |
                                                (fn.lower(Aliases.alias85) == message) |
                                                (fn.lower(Aliases.alias86) == message) |
                                                (fn.lower(Aliases.alias87) == message) |
                                                (fn.lower(Aliases.alias88) == message) |
                                                (fn.lower(Aliases.alias89) == message) |
                                                (fn.lower(Aliases.alias90) == message) |
                                                (fn.lower(Aliases.alias91) == message) |
                                                (fn.lower(Aliases.alias92) == message) |
                                                (fn.lower(Aliases.alias93) == message) |
                                                (fn.lower(Aliases.alias94) == message) |
                                                (fn.lower(Aliases.alias95) == message) |
                                                (fn.lower(Aliases.alias96) == message) |
                                                (fn.lower(Aliases.alias97) == message) |
                                                (fn.lower(Aliases.alias98) == message) |
                                                (fn.lower(Aliases.alias99) == message) |
                                                (fn.lower(Aliases.alias100) == message))).execute()
    return check_aliases


def log(func):
    logger = logging.getLogger(func.__module__)

    @functools.wraps(func)
    def decorator(self, *args, **kwargs):
        logger.info('Entering: %s', func.__name__)
        logger.info(args[0])
        result = func(self, *args, **kwargs)
        logger.info('Exiting: %s', func.__name__)
        return result
    return decorator
