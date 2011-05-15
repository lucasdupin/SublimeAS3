/**
 * AS3 Syntax
 * http://yourpalmark.com/
 *
 * @author
 * Mark Walters
 */
SyntaxHighlighter.brushes.AS3 = function()
{
	var definitions =	'class interface package';
	
	var keywords =	'Array Boolean Date decodeURI decodeURIComponent encodeURI encodeURIComponent escape ' +
					'int isFinite isNaN isXMLName Number Object parseFloat parseInt ' +
					'String uint unescape XML XMLList ' + //global functions
					
					'Infinity -Infinity NaN undefined ' + //global constants
					
					'as delete instanceof is new typeof ' + //operators
					
					'break case catch continue default do each else finally for if in ' +
					'label return super switch throw try while with ' + //statements
					
					'dynamic final internal native override private protected public static ' + //attributes
					
					'...rest const extends get implements namespace set ' + //definitions
					
					'import include use ' + //directives
					
					'AS3 flash_proxy object_proxy ' + //namespaces
					
					'false null this true ' + //expressions
					
					'void Null'; //types
	
	this.regexList = [
		{ regex: SyntaxHighlighter.regexLib.singleLineCComments,	css: 'comments' },			// one line comments
		{ regex: SyntaxHighlighter.regexLib.multiLineCComments,		css: 'blockcomments' },		// multiline comments
		{ regex: SyntaxHighlighter.regexLib.doubleQuotedString,		css: 'string' },			// double quoted strings
		{ regex: SyntaxHighlighter.regexLib.singleQuotedString,		css: 'string' },			// single quoted strings
		{ regex: /\s*#.*/gm,										css: 'preprocessor' },		// preprocessor tags like #region and #endregion
		{ regex: new RegExp(this.getKeywords(definitions), 'gm'),	css: 'definition' },		// definitions
		{ regex: new RegExp(this.getKeywords(keywords), 'gm'),		css: 'keyword' },			// keywords
		{ regex: new RegExp('var', 'gm'),							css: 'variable' },			// variable
		{ regex: new RegExp('function', 'gm'),						css: 'function' },			// function
		{ regex: new RegExp('trace', 'gm'),							css: 'trace' }				// trace
		];
	
	this.forHtmlScript(SyntaxHighlighter.regexLib.scriptScriptTags);
};

SyntaxHighlighter.brushes.AS3.prototype	= new SyntaxHighlighter.Highlighter();
SyntaxHighlighter.brushes.AS3.aliases	= ['as', 'actionscript', 'ActionScript', 'as3', 'AS3'];
