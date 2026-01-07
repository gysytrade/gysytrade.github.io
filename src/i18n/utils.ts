import { ui, defaultLang } from './ui';

export function getLangFromUrl(url: URL) {
    const [, lang] = url.pathname.split('/');
    if (lang in ui) return lang as keyof typeof ui;
    // If no language prefix or invalid language, return default language (zh)
    return defaultLang;
}

export function useTranslations(lang: keyof typeof ui) {
    return function t(key: keyof typeof ui[typeof defaultLang]) {
        return ui[lang][key] || ui[defaultLang][key];
    }
}

export function getRouteFromUrl(url: URL): string | undefined {
    const [, lang, ...rest] = url.pathname.split('/');
    if (lang in ui) {
        return rest.join('/');
    }
    return undefined;
}

export function getLocalizedPath(path: string, lang: string) {
    // Ensure path starts with /
    const normalizedPath = path.startsWith('/') ? path : `/${path}`;
    // If default lang (zh), return path as is (assuming root is zh)
    // If other lang, prepend /lang
    // Handle root path specially if needed, but usually /en/ works for /en
    if (lang === defaultLang) {
        return normalizedPath;
    }
    return `/${lang}${normalizedPath === '/' ? '' : normalizedPath}`;
}
