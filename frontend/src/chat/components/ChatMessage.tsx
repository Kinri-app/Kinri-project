import type { AIChatMessage } from "../types/chatTypes.ts";
import React, { useEffect, useMemo, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

const CodeBlock: React.FC<{
    inline?: boolean;
    className?: string;
    children: React.ReactNode;
    }> = ({ inline, className, children }) => {
    const language = /language-(\w+)/.exec(className || "")?.[1] || "";
    const codeText = React.Children.toArray(children)
        .map((c) =>
        typeof c === "string" || typeof c === "number" ? String(c) : ""
        )
        .join("");

    const handleCopy = async () => {
        try {
        await navigator.clipboard.writeText(codeText);
        } catch (err) {
        console.debug("copy failed", err);
        }
    };

    if (inline) {
        return (
        <code
            className={`px-1 py-0.5 rounded bg-gray-800/70 text-gray-100 text-[0.9em] ${
            className || ""
            }`}
        >
            {children}
        </code>
        );
    }

    return (
        <div className="relative my-2">
        <pre className="rounded bg-black/80 text-gray-100 p-3 overflow-auto text-sm">
            <code className={className}>{children}</code>
        </pre>
        <button
            onClick={handleCopy}
            className="absolute top-1 right-1 bg-white/90 px-2 py-1 text-xs rounded shadow"
            aria-label="Copy code"
            type="button"
        >
            Copy
        </button>
        {language && (
            <div className="absolute top-1 left-1 text-[0.6rem] uppercase tracking-wide text-gray-300 px-1.5 py-0.5 bg-black/50 rounded">
            {language}
            </div>
        )}
        </div>
    );
    };

    import type { ComponentPropsWithoutRef } from "react";
    
    const CodeRenderer: React.FC<ComponentPropsWithoutRef<"code"> & { inline?: boolean }> = ({ inline, className, children, ...props }) => (
        <CodeBlock inline={inline} className={className} {...props}>
            {children}
        </CodeBlock>
    );

    const LinkRenderer: React.FC<ComponentPropsWithoutRef<"a">> = ({
    href,
    children,
    ...rest
    }) => (
    <a
        href={String(href)}
        target="_blank"
        rel="noopener noreferrer"
        className="underline decoration-dotted hover:decoration-solid"
        {...rest}
    >
        {children}
    </a>
    );

    const ChatMessage = ({ role, content }: AIChatMessage) => {
    const isUser = role === "user";

    const [rehypeSanitizePlugin, setRehypeSanitizePlugin] = useState<any>(null);

    useEffect(() => {
        let mounted = true;
        import("rehype-sanitize")
        .then((mod) => {
            if (mounted) setRehypeSanitizePlugin(mod.default || mod);
        })
        .catch(() => {
            setRehypeSanitizePlugin(null);
        });

        return () => {
        mounted = false;
        };
    }, []);

    const rehypePlugins = useMemo(
        () => (rehypeSanitizePlugin ? [rehypeSanitizePlugin] : []),
        [rehypeSanitizePlugin]
    );

    return (
        <div
        className={`w-full flex gap-3 text-sm ${
            isUser ? "justify-end" : "justify-start"
        }`}
        >
        {/* USER BUBBLE */}
        {isUser && (
            <div className="max-w-[80%] px-4 py-2 rounded-lg shadow-sm bg-gray-100 text-gray-900">
            <p className="font-medium text-gray-800 mb-1">You</p>
            <p className="whitespace-pre-wrap break-words">{content}</p>
            </div>
        )}

        {/* ECHO BUBBLE */}
        {!isUser && (
            <div className="max-w-[80%] px-4 py-3 rounded-lg shadow-sm bg-zinc-900 text-gray-100">
            <p className="font-medium text-gray-100 mb-1">Echo</p>
            <div className="prose prose-invert prose-sm max-w-none break-words">
                <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                rehypePlugins={rehypePlugins}
                components={{
                    code: CodeRenderer,
                    a: LinkRenderer,
                }}
                >
                {content}
                </ReactMarkdown>
            </div>
            {!rehypeSanitizePlugin && (
                <div className="text-[0.6rem] text-yellow-400 mt-1">
                Sanitizer not loaded — install <code>rehype-sanitize</code> for production.
                </div>
            )}
            </div>
        )}
        </div>
    );
    };

export default React.memo(ChatMessage);
