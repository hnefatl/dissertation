# TODOs to write about

- Need an implementation chapter section for the repository structure.

- Closure implementation is slow: no surprises, it's a class and has to be designed to take arrays and lists and stuff,
  where raw languages can just manipulate heap objects directly to add arguments. JVM definitely gets in the way here.

- Typeclass polymorphism is known at runtime, so no need for dynamic dispatch and vtables at runtime -> cheaper.
  Except.... have to unbox the impls so still some overhead. Talk about how inlining would happily eliminate that cost.

- Type description: `TypeApp` isn't function application, that's represented by a tree as `->` can be treated as a type
  constructor like everything else. Clarify, also demonstrates that things aren't obvious.

- Typechecking bug with multiparameter datatypes:

      fmap f (Right x) = Right (f x)  -- :: (b -> c) -> Either a b -> Either a c
      fmap _ l = l                    -- :: a -> b -> b
      fmap _ (Left x) = Left x        -- :: (b -> d) -> Either a b -> Either c d

  Middle implementation forces the types to unify to `(b -> b) -> Either a b -> Either a b`.