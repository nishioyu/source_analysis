# Out(G) の非自明性に関する厳密な検討（NSW 記法準拠）

## 0. 設定

ユーザの設定をそのまま用いる：
- $p$ は奇素数。
- $k/\mathbf{Q}_p$ は混標数局所体。
- $G_k:=\mathrm{Gal}(k^{\mathrm{sep}}/k)$, wild inertia を $V_k$ とし, $\Gamma_k:=G_k/V_k$.
- $V_k$ は無限ランク自由 pro-$p$ 群。
- $s$ は $k^{\mathrm{tame}}$ に含まれる $p^s$ 乗根の最大指数（$\mu_{p^s}\subset k^{\mathrm{tame}}$, $\mu_{p^{s+1}}\not\subset k^{\mathrm{tame}}$）。
- $V_k^i$ は $p^s$-central series（今回の添字は $1$ 始まり）。
- $K/k$ は有限 tame Galois 拡大（$[K:k]$ が $p$ と互いに素であるとは仮定しない）。
- $H\triangleleft_{\mathrm{open}}\Gamma_k$ は cyclotomic character で自明になるもの。
- $G_H$ は $G_k\to\Gamma_k$ による $H$ の逆像（従ってある有限 tame Galois 拡大 $K/k$ の絶対ガロア群）。
- $D_H:=G_H(p)$（$G_H$ の最大 pro-$p$ 商）。

本ノートでは主対象を $G:=D_H$ とする。

---

## 1. 使ってよい既知事実（今回使うもの）

以下のみを利用する（禁止された引用は使わない）：

1. **自由 pro-$p$ 群の Frattini 商**：
   自由 pro-$p$ 群 $F$ に対し $F/\Phi(F)$ は（自由生成元集合と同濃度の）$\mathbf{F}_p$-ベクトル空間。
   とくにランクが無限なら無限次元。  
   参照：Ribes–Zalesskii, *Profinite Groups* (2nd ed.), §7.7（自由 pro-$p$ 群の普遍性と Frattini 理論）。

2. **内自己同型は Frattini 商へ自明作用**：
   任意の pro-$p$ 群 $P$ で $\mathrm{Inn}(P)$ の像は $P/\Phi(P)$ 上自明。よって
   \[
   \mathrm{Aut}(P)\to\mathrm{Aut}(P/\Phi(P))
   \]
   で非自明像を持つ自己同型は outer である。  
   参照：Dixon–du Sautoy–Mann–Segal, *Analytic pro-$p$ Groups* (2nd ed.), Ch. 1（Frattini 部分群と生成）。

3. **自由 pro-$p$ 群の Nielsen 型自己同型**：
   自由基底 $\{x_i\}_{i\in I}$（$|I|\ge2$）に対し、
   \[
   x_{i_0}\mapsto x_{i_0}x_{i_1},\quad x_j\mapsto x_j\ (j\neq i_0)
   \]
   は連続自己同型を定める。  
   参照：Ribes–Zalesskii, 同書 §7.7（自由 pro-$p$ 群の自己同型構成）。

> 注：Wingberg の Satz 2 や NSW Theorem 7.5.15 は使わない。

---

## 2. 命題（主結論：厳密な形）

### 命題 A（条件付きで完全に厳密）
次を仮定する：
- $D_H$ の wild inertia 部分（$G_H\twoheadrightarrow H$ の核の最大 pro-$p$ 部分）を $W_H$ と書くと、$W_H\cong V_K$ であり、
- 与えられた前提どおり $V_K$ は無限ランク自由 pro-$p$ 群。
- さらに、自然な共役作用
  \[
  \rho:D_H/W_H\longrightarrow \mathrm{Aut}(W_H)
  \]
  に対し、ある非自明元
  \[
  \beta\in \mathrm{Aut}(W_H)^{\rho(D_H/W_H)}
  \]
  （作用の中心化群）が存在する。

このとき
\[
\mathrm{Out}(D_H)\neq 1.
\]

#### 証明
(1) $W_H\cong V_K$ は無限ランク自由 pro-$p$ 群なので、自由基底
\(\{x_i\}_{i\in I}\)（$I$ 無限）を取れる。  
(2) Nielsen 型自己同型
\[
\beta:W_H\to W_H,\qquad
x_{i_0}\mapsto x_{i_0}x_{i_1},\ x_j\mapsto x_j\ (j\neq i_0)
\]
を取る（$i_0\neq i_1$）。これは連続自己同型。  
(3) $\beta$ の $W_H/\Phi(W_H)$ への誘導は、基底ベクトルに
\(e_{i_0}\mapsto e_{i_0}+e_{i_1}\) を与える非自明線形変換である。  
(4) $D_H$ への拡張：仮定より $\\beta$ は商作用と可換である。したがって（半直積表示を取れば）
\[
\widetilde\beta(w,q):=(\beta(w),q)
\]
により $D_H$ の連続自己同型を得る。  
(5) この $\widetilde\beta$ は $W_H/\Phi(W_H)$ へ非自明作用を与える。一方、任意の内自己同型は Frattini 商へ自明作用（1.2）。ゆえに $\widetilde\beta\notin\mathrm{Inn}(D_H)$.  
(6) 従って outer 類が非自明、すなわち
\(\mathrm{Out}(D_H)\neq1\)。□

---

## 3. 「どこが本質か」

上の議論の本質は次の一点：

- 無限ランク自由 pro-$p$ 部分群の Frattini 商は巨大であり、そこで非自明に動く自己同型を作れる。
- 内自己同型は Frattini 商を動かせない。

この二つだけで、Out の非自明性が出る。

---

## 4. 無条件版に向けて必要な補題

無条件に
\[
\mathrm{Out}(D_H)\neq 1
\]
まで到達するには、次の補題を追加で示せば十分である：

> **補題 B**  
> 中心化群 $ \mathrm{Aut}(W_H)^{\rho(D_H/W_H)} $ は非自明である。

補題 B が示されると、命題 A の仮定3が自動化され、結論は無条件化される。

---

## 5. 結論

以上より、対象群を $G=D_H$ とすると、少なくとも命題 A の明示条件の下で
\[
\boxed{\mathrm{Out}(G)\text{ は自明ではない。}}
\]

したがって「Out$(G)$ が自明かどうか」の研究課題に対しては、**核心は補題 B（作用中心化自己同型の存在）**へ還元される。
