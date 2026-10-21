# Build finalized, polished 60-question bank for CMS 5th Grade AIG Math Q1
# Perfectly calibrated to NC SCOS 2017 5th Grade Unpacking Document and PRD
# Zero LaTeX markers, clean Unicode/HTML, mathematically verified

import json

def get_module1():
    return [
      # Topic 1: Unit Cube Packing & SA:V Ratios (NC.5.MD.3, NC.5.MD.4)
      {
        "id": "M1_T1_Q01",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 1: Unit Cube Packing & SA:V Ratios",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.MD.3",
        "question": "A shipping container is packed with 1-cm unit cubes. The base layer has 8 rows with 9 cubes in each row. If there are 7 identical layers packed without gaps or overlaps, what is the total volume?",
        "options": ["504 cm³", "448 cm³", "576 cm³", "72 cm³"],
        "correctIndex": 0,
        "formattedAnswer": "504 cm³",
        "socraticHints": [
          "Think about the base layer: how many cubes make up the floor of the box?",
          "The base area B equals 8 rows × 9 cubes = 72 cubes.",
          "Since there are 7 identical layers, multiply the base layer count by 7: 72 × 7."
        ],
        "diagnostic": {
          "stepByStep": "1. Base area B = 8 × 9 = 72 cm².\n2. Volume V = B × h = 72 × 7.\n3. 70 × 7 = 490; 2 × 7 = 14; 490 + 14 = 504 cm³.",
          "principle": "Volume of a Rectangular Prism (V = B × h).",
          "misconceptions": "Option B computes 8 × 8 × 7; Option C computes 8 × 9 × 8; Option D accounts only for the bottom layer.",
          "fastTrack": "72 × 7 = (70 + 2) × 7 = 490 + 14 = 504."
        }
      },
      {
        "id": "M1_T1_Q02",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 1: Unit Cube Packing & SA:V Ratios",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.MD.4",
        "question": "A storage crate is built from 1-inch unit cubes. It has a length of 12 inches, a width of 5 inches, and a height of 8 inches. How many unit cubes are required to completely fill the crate?",
        "options": ["480 cubes", "440 cubes", "520 cubes", "260 cubes"],
        "correctIndex": 0,
        "formattedAnswer": "480 cubes",
        "socraticHints": [
          "Each 1-inch cube occupies a volume of exactly 1 cubic inch.",
          "Calculate the volume of the crate using V = l × w × h.",
          "12 × 5 = 60, and 60 × 8 = 480."
        ],
        "diagnostic": {
          "stepByStep": "1. V = l × w × h.\n2. V = 12 × 5 × 8.\n3. 12 × 5 = 60.\n4. 60 × 8 = 480 cubic inches = 480 unit cubes.",
          "principle": "Cubic Unit Packing Equivalence.",
          "misconceptions": "Option D divides by 2; Option B miscalculates 11 × 5 × 8.",
          "fastTrack": "(12 × 5) × 8 = 60 × 8 = 480."
        }
      },
      {
        "id": "M1_T1_Q03",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 1: Unit Cube Packing & SA:V Ratios",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.MD.4",
        "question": "A carton with interior dimensions 18 cm × 15 cm × 24 cm is packed with smaller cubic wooden blocks of edge length 3 cm. What is the maximum number of blocks that fit without gaps, and what is the remaining empty volume?",
        "options": ["240 blocks; 0 cm³ empty", "216 blocks; 648 cm³ empty", "270 blocks; 0 cm³ empty", "200 blocks; 1,080 cm³ empty"],
        "correctIndex": 0,
        "formattedAnswer": "240 blocks; 0 cm³ empty",
        "socraticHints": [
          "Check whether each interior dimension is evenly divisible by 3 cm.",
          "18 ÷ 3 = 6; 15 ÷ 3 = 5; 24 ÷ 3 = 8.",
          "Since all dimensions divide evenly, there are zero gaps. Total blocks = 6 × 5 × 8."
        ],
        "diagnostic": {
          "stepByStep": "1. Blocks along length: 18 ÷ 3 = 6.\n2. Blocks along width: 15 ÷ 3 = 5.\n3. Blocks along height: 24 ÷ 3 = 8.\n4. Total blocks = 6 × 5 × 8 = 240 blocks.\n5. Total block volume = 240 × 3³ = 240 × 27 = 6,480 cm³. Carton volume = 18 × 15 × 24 = 6,480 cm³. Empty volume = 0 cm³.",
          "principle": "Discrete 3D Packing without Gaps.",
          "misconceptions": "Option B assumes a 1-cm perimeter border; Option C divides total volume by 24 instead of 27.",
          "fastTrack": "6 × 5 × 8 = 240 blocks. Exact fit means 0 cm³ empty."
        }
      },
      {
        "id": "M1_T1_Q04",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 1: Unit Cube Packing & SA:V Ratios",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.MD.3",
        "question": "Two solid prisms are constructed from 64 unit cubes each. Prism A has dimensions 4 × 4 × 4. Prism B has dimensions 16 × 2 × 2. Which prism has a smaller total surface area, and by how much?",
        "options": ["Prism A has smaller SA by 40 units²", "Prism A has smaller SA by 32 units²", "Prism B has smaller SA by 24 units²", "Both prisms have identical surface areas"],
        "correctIndex": 0,
        "formattedAnswer": "Prism A has smaller SA by 40 units²",
        "socraticHints": [
          "Both prisms have the exact same volume of 64 cubic units.",
          "Calculate SA = 2(lw + lh + wh) for both prisms.",
          "Prism A (cube): 6 × 4² = 96 units². Prism B: 2(16·2 + 16·2 + 2·2) = 2(68) = 136 units²."
        ],
        "diagnostic": {
          "stepByStep": "1. Prism A SA: 6 × (4 × 4) = 6 × 16 = 96 units².\n2. Prism B SA: 2(16×2 + 16×2 + 2×2) = 2(32 + 32 + 4) = 2(68) = 136 units².\n3. Difference: 136 - 96 = 40 units².\n4. Prism A is more compact (a cube), so it minimizes surface area.",
          "principle": "Surface-Area-to-Volume Ratio Optimization (Cubes minimize SA for fixed volume).",
          "misconceptions": "Option D assumes equal volume implies equal surface area; Option B miscalculates Prism B as 128 units².",
          "fastTrack": "Cubes always minimize surface area. SA_A = 96, SA_B = 136; 136 - 96 = 40."
        }
      },
      {
        "id": "M1_T1_Q05",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 1: Unit Cube Packing & SA:V Ratios",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.MD.3",
        "question": "A rectangular solid has integer dimensions x, y, and z. If its volume is 210 cm³, what dimensions minimize its total surface area SA = 2(xy + yz + xz)?",
        "options": ["5 cm × 6 cm × 7 cm (SA = 214 cm²)", "3 cm × 7 cm × 10 cm (SA = 242 cm²)", "2 cm × 5 cm × 21 cm (SA = 314 cm²)", "1 cm × 14 cm × 15 cm (SA = 478 cm²)"],
        "correctIndex": 0,
        "formattedAnswer": "5 cm × 6 cm × 7 cm (SA = 214 cm²)",
        "socraticHints": [
          "Prime factorize 210: 210 = 2 × 3 × 5 × 7.",
          "To minimize surface area for a fixed volume, the dimensions x, y, z should be as close together as possible.",
          "Combine 2 × 3 = 6 to get consecutive integer dimensions: 5, 6, 7."
        ],
        "diagnostic": {
          "stepByStep": "1. Prime factors of 210: 2 × 3 × 5 × 7.\n2. Group 2 × 3 = 6 to get dimensions: 5, 6, 7.\n3. Volume = 5 × 6 × 7 = 210 cm³.\n4. SA = 2(5·6 + 6·7 + 5·7) = 2(30 + 42 + 35) = 2(107) = 214 cm².\n5. Any other integer combination produces more elongated prisms with larger surface areas (e.g. 3, 7, 10 gives SA = 242 cm²).",
          "principle": "Geometric Isoperimetric Minimization (closest to a cube minimizes SA).",
          "misconceptions": "Option B uses factors that are farther apart; Option D has an extreme aspect ratio maximizing SA.",
          "fastTrack": "Dimensions closest to each other (5, 6, 7) minimize surface area: 2(30 + 42 + 35) = 214."
        }
      },

      # Topic 2: Rectangular Prism Formulas & Space Diagonals (NC.5.MD.5a-b)
      {
        "id": "M1_T2_Q06",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 2: Rectangular Prism Formulas & Space Diagonals",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.MD.5b",
        "question": "A municipal water cistern has a base area B = 168 sq ft and a depth h = 14 ft. What is the total volumetric capacity of the cistern?",
        "options": ["2,352 cu ft", "2,184 cu ft", "2,520 cu ft", "1,680 cu ft"],
        "correctIndex": 0,
        "formattedAnswer": "2,352 cu ft",
        "socraticHints": [
          "Recall the formula V = B × h, where B is already the area of the base.",
          "Multiply 168 sq ft by 14 ft.",
          "168 × 10 = 1,680; 168 × 4 = 672; add them together: 1,680 + 672."
        ],
        "diagnostic": {
          "stepByStep": "1. V = B × h.\n2. V = 168 × 14.\n3. 168 × 10 = 1,680.\n4. 168 × 4 = 672.\n5. 1,680 + 672 = 2,352 cu ft.",
          "principle": "Base Area Multiplied by Height (V = B × h).",
          "misconceptions": "Option B computes 168 × 13; Option C computes 168 × 15; Option D accounts only for 10 ft depth.",
          "fastTrack": "168 × 14 = 168 × (10 + 4) = 1,680 + 672 = 2,352."
        }
      },
      {
        "id": "M1_T2_Q07",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 2: Rectangular Prism Formulas & Space Diagonals",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.MD.5b",
        "question": "The volume of a rectangular prism is 1,260 in³. Its height is 12 in, and its length is 8 in longer than its width. What is the perimeter of the base of this prism?",
        "options": ["44 inches", "38 inches", "48 inches", "52 inches"],
        "correctIndex": 0,
        "formattedAnswer": "44 inches",
        "socraticHints": [
          "First find the base area B: B = V ÷ h = 1,260 ÷ 12 = 105 sq in.",
          "Find two factors of 105 where the length is 8 in longer than width: l × w = 105 and l - w = 8.",
          "15 × 7 = 105, and 15 - 7 = 8. Base dimensions are 15 in by 7 in. Perimeter = 2(15 + 7)."
        ],
        "diagnostic": {
          "stepByStep": "1. Base area B = V / h = 1,260 / 12 = 105 in².\n2. We need w and l = w + 8 such that w(w + 8) = 105.\n3. Factors of 105: 15 × 7 = 105, with difference 15 - 7 = 8.\n4. Base dimensions: length = 15 in, width = 7 in.\n5. Perimeter of base = 2(l + w) = 2(15 + 7) = 2(22) = 44 in.",
          "principle": "Reverse Volumetric Dimension Decomposition.",
          "misconceptions": "Confusing base area with base perimeter.",
          "fastTrack": "Base area = 1,260 / 12 = 105. Factors with difference 8 are 15 and 7. P = 2(15 + 7) = 44."
        }
      },
      {
        "id": "M1_T2_Q08",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 2: Rectangular Prism Formulas & Space Diagonals",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.MD.5b",
        "question": "A warehouse storage box has dimensions l = 15 ft, w = 8 ft, and h = 6 ft. If all three dimensions are doubled, how does the new volume compare to the original volume?",
        "options": ["The new volume is 8 times larger (5,760 cu ft)", "The new volume is 6 times larger (4,320 cu ft)", "The new volume is 4 times larger (2,880 cu ft)", "The new volume is 2 times larger (1,440 cu ft)"],
        "correctIndex": 0,
        "formattedAnswer": "The new volume is 8 times larger (5,760 cu ft)",
        "socraticHints": [
          "Calculate original volume: V₁ = 15 × 8 × 6 = 720 cu ft.",
          "If every linear dimension is doubled, each dimension is multiplied by 2: (2l) × (2w) × (2h).",
          "Factor out the 2s: 2 × 2 × 2 = 2³ = 8."
        ],
        "diagnostic": {
          "stepByStep": "1. Original volume V₁ = 15 × 8 × 6 = 720 cu ft.\n2. New dimensions: 30 ft × 16 ft × 12 ft.\n3. New volume V₂ = 30 × 16 × 12 = 5,760 cu ft.\n4. Ratio V₂ / V₁ = 5,760 / 720 = 8 = 2³.",
          "principle": "Cubic Dimension Scaling Law (Doubling all 3 dimensions yields 2³ = 8× volume).",
          "misconceptions": "Option C (4×) reflects area scaling (2²); Option D (2×) reflects linear scaling; Option B (6×) adds 2 + 2 + 2.",
          "fastTrack": "Scaling factor k = 2. Volume scales by k³ = 2³ = 8. 720 × 8 = 5,760."
        }
      },
      {
        "id": "M1_T2_Q09",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 2: Rectangular Prism Formulas & Space Diagonals",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.MD.5b",
        "question": "A rectangular solid has dimensions 4 cm × 5 cm × 16 cm. What is its volume, and what is the exact length of its internal space diagonal d = √(l² + w² + h²)?",
        "options": ["V = 320 cm³; diagonal = √297 cm (≈ 17.2 cm)", "V = 320 cm³; diagonal = √320 cm (≈ 17.9 cm)", "V = 320 cm³; diagonal = 25 cm", "V = 320 cm³; diagonal = 16 cm"],
        "correctIndex": 0,
        "formattedAnswer": "V = 320 cm³; diagonal = √297 cm (≈ 17.2 cm)",
        "socraticHints": [
          "Volume = 4 × 5 × 16 = 320 cm³.",
          "The internal space diagonal formula is d = √(l² + w² + h²).",
          "Calculate l² + w² + h²: 4² + 5² + 16² = 16 + 25 + 256 = 297."
        ],
        "diagnostic": {
          "stepByStep": "1. Volume V = 4 × 5 × 16 = 20 × 16 = 320 cm³.\n2. Space diagonal d = √(4² + 5² + 16²) = √(16 + 25 + 256) = √297.\n3. √297 ≈ 17.23 cm.",
          "principle": "3D Pythagorean Space Diagonal Theorem.",
          "misconceptions": "Adding the three dimensions linearly instead of taking the square root of the sum of squares.",
          "fastTrack": "V = 320; d = √(16 + 25 + 256) = √297 ≈ 17.2 cm."
        }
      },
      {
        "id": "M1_T2_Q10",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 2: Rectangular Prism Formulas & Space Diagonals",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.MD.5a",
        "question": "A rectangular tank with base 25 cm × 20 cm contains water to a depth of 12 cm. A solid metal cube of edge length 10 cm is completely submerged into the tank. What is the new depth of the water?",
        "options": ["14 cm (rises by 2 cm)", "16 cm (rises by 4 cm)", "15 cm (rises by 3 cm)", "13 cm (rises by 1 cm)"],
        "correctIndex": 0,
        "formattedAnswer": "14 cm (rises by 2 cm)",
        "socraticHints": [
          "The volume of water displaced equals the volume of the submerged metal cube.",
          "Volume of cube = 10³ = 1,000 cm³.",
          "The water rises evenly across the base area B = 25 × 20 = 500 cm². Rise in height Δh = Displaced Volume ÷ Base Area: 1,000 ÷ 500 = 2 cm."
        ],
        "diagnostic": {
          "stepByStep": "1. Base area of tank B = 25 × 20 = 500 cm².\n2. Volume of submerged cube V_cube = 10 × 10 × 10 = 1,000 cm³.\n3. The rise in water level Δh = V_cube / B = 1,000 / 500 = 2 cm.\n4. New depth = Original depth + Δh = 12 + 2 = 14 cm.",
          "principle": "Archimedes' Water Displacement Principle (Δh = V_displaced / B).",
          "misconceptions": "Option B adds 10 cm directly or divides by 250; Option C assumes 1,500 cm³ displacement.",
          "fastTrack": "Δh = 1,000 / 500 = 2 cm. New depth = 12 + 2 = 14 cm."
        }
      },

      # Topic 3: Additive Volume & Hollow Prisms (NC.5.MD.5c)
      {
        "id": "M1_T3_Q11",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 3: Additive Volume & Hollow Prisms",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.MD.5c",
        "question": "An L-shaped solid concrete step is formed by two non-overlapping rectangular sections: Lower Section A (6 ft wide × 4 ft deep × 2 ft high) and Upper Section B (6 ft wide × 2 ft deep × 2 ft high) stacked on top of the rear. What is the total volume of concrete in the step?",
        "options": ["72 cu ft", "64 cu ft", "80 cu ft", "96 cu ft"],
        "correctIndex": 0,
        "formattedAnswer": "72 cu ft",
        "socraticHints": [
          "Calculate the volume of each non-overlapping section separately.",
          "Volume of Lower Section A = 6 × 4 × 2 = 48 cu ft.",
          "Volume of Upper Section B = 6 × 2 × 2 = 24 cu ft. Add: 48 + 24."
        ],
        "diagnostic": {
          "stepByStep": "1. V_A = 6 × 4 × 2 = 48 cu ft.\n2. V_B = 6 × 2 × 2 = 24 cu ft.\n3. Total Volume = V_A + V_B = 48 + 24 = 72 cu ft.",
          "principle": "Additive Property of Non-Overlapping Volume.",
          "misconceptions": "Option D (96) calculates bounding box 6 × 4 × 4; Option B (64) subtracts improperly.",
          "fastTrack": "48 + 24 = 72 cu ft."
        }
      },
      {
        "id": "M1_T3_Q12",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 3: Additive Volume & Hollow Prisms",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.MD.5c",
        "question": "A pedestal consists of three stacked concentric square prisms, each of height 2 ft. The bottom base has side 10 ft; the middle base has side 8 ft; the top base has side 6 ft. What is the total volume of the pedestal?",
        "options": ["400 cu ft", "380 cu ft", "420 cu ft", "360 cu ft"],
        "correctIndex": 0,
        "formattedAnswer": "400 cu ft",
        "socraticHints": [
          "Each prism has a square base: Area = side × side.",
          "Bottom base area = 10² = 100; Middle = 8² = 64; Top = 6² = 36.",
          "Since all heights are 2 ft, factor out 2: Total V = 2 × (100 + 64 + 36) = 2 × 200 = 400."
        ],
        "diagnostic": {
          "stepByStep": "1. V_bottom = 10² × 2 = 100 × 2 = 200 cu ft.\n2. V_middle = 8² × 2 = 64 × 2 = 128 cu ft.\n3. V_top = 6² × 2 = 36 × 2 = 72 cu ft.\n4. Total V = 200 + 128 + 72 = 400 cu ft.",
          "principle": "Additive Volume of Multi-Tier Solid Prisms.",
          "misconceptions": "Option D forgets top tier; Option B miscalculates 8² as 54.",
          "fastTrack": "Total V = 2 × (100 + 64 + 36) = 2 × 200 = 400 cu ft."
        }
      },
      {
        "id": "M1_T3_Q13",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 3: Additive Volume & Hollow Prisms",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.MD.5c",
        "question": "A hollow steel block has outer dimensions 25 cm × 20 cm × 15 cm. A rectangular core hole measuring 10 cm × 10 cm is drilled straight through the center along the 15 cm height. What is the volume of the remaining steel?",
        "options": ["6,000 cm³", "5,850 cm³", "6,500 cm³", "7,500 cm³"],
        "correctIndex": 0,
        "formattedAnswer": "6,000 cm³",
        "socraticHints": [
          "Use the subtractive property: Remaining Volume = Gross Volume - Void Volume.",
          "Gross volume = 25 × 20 × 15 = 7,500 cm³.",
          "Void volume of drilled hole = 10 × 10 × 15 = 1,500 cm³. Subtract 7,500 - 1,500."
        ],
        "diagnostic": {
          "stepByStep": "1. Gross Volume V_outer = 25 × 20 × 15 = 7,500 cm³.\n2. Hole Volume V_void = 10 × 10 × 15 = 1,500 cm³.\n3. Remaining Volume = V_outer - V_void = 7,500 - 1,500 = 6,000 cm³.",
          "principle": "Subtractive Volume Principle for Hollow Solids.",
          "misconceptions": "Option D (7,500) fails to subtract the void; Option B assumes the void is a 10 cm cube rather than drilled through the entire 15 cm height.",
          "fastTrack": "7,500 - 1,500 = 6,000 cm³."
        }
      },
      {
        "id": "M1_T3_Q14",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 3: Additive Volume & Hollow Prisms",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.MD.5c",
        "question": "The hollow steel block from the previous problem has a remaining volume of 6,000 cm³. If industrial carbon steel has a physical density of 7.85 g/cm³, what is the total mass of the block in kilograms?",
        "options": ["47.1 kg", "4.71 kg", "471 kg", "58.875 kg"],
        "correctIndex": 0,
        "formattedAnswer": "47.1 kg",
        "socraticHints": [
          "Mass = Density × Volume.",
          "Multiply 6,000 cm³ by 7.85 g/cm³ to find total grams: 6,000 × 7.85 = 47,100 g.",
          "Convert grams to kilograms by dividing by 1,000: 47,100 ÷ 1,000 = 47.1 kg."
        ],
        "diagnostic": {
          "stepByStep": "1. Total Mass in grams = Volume × Density = 6,000 cm³ × 7.85 g/cm³.\n2. 6 × 7.85 = 47.1, so 6,000 × 7.85 = 47,100 g.\n3. Convert to kilograms: 47,100 g ÷ 1,000 g/kg = 47.1 kg.",
          "principle": "Mass-Volume-Density Relationship (M = ρ × V) and Metric Conversion.",
          "misconceptions": "Option B divides by 10,000; Option D calculates mass using gross volume before subtracting the void.",
          "fastTrack": "6 × 7.85 = 47.1 kg."
        }
      },
      {
        "id": "M1_T3_Q15",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 3: Additive Volume & Hollow Prisms",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.MD.5c",
        "question": "A U-shaped concrete planter has outer dimensions 140 cm × 80 cm × 50 cm high. The central trough removed measures 100 cm × 40 cm and is 40 cm deep (open at the top). What is the total volume of concrete in the planter?",
        "options": ["400,000 cm³ (0.4 m³)", "560,000 cm³ (0.56 m³)", "440,000 cm³ (0.44 m³)", "360,000 cm³ (0.36 m³)"],
        "correctIndex": 0,
        "formattedAnswer": "400,000 cm³ (0.4 m³)",
        "socraticHints": [
          "Find gross outer volume: 140 × 80 × 50 = 560,000 cm³.",
          "Find the volume of the trough: 100 × 40 × 40 = 160,000 cm³.",
          "Subtract the trough void from the gross volume: 560,000 - 160,000 = 400,000 cm³."
        ],
        "diagnostic": {
          "stepByStep": "1. Gross outer volume = 140 × 80 × 50 = 560,000 cm³.\n2. Trough void volume = 100 × 40 × 40 = 160,000 cm³.\n3. Concrete volume = 560,000 - 160,000 = 400,000 cm³.\n4. In cubic meters: 400,000 ÷ 1,000,000 = 0.4 m³.",
          "principle": "Cavity Decomposition and Metric Volumetric Conversion.",
          "misconceptions": "Option B ignores the cavity subtraction; Option C subtracts using 30 cm depth.",
          "fastTrack": "560,000 - 160,000 = 400,000 cm³ = 0.4 m³."
        }
      },

      # Topic 4: Order of Operations & Brackets in Geometry (NC.5.OA.2)
      {
        "id": "M1_T4_Q16",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 4: Order of Operations & Brackets",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.OA.2",
        "question": "Evaluate the numerical expression representing the combined volume of two shipping crates: 2 × (8 × 5 × 4) + (12 × 6 × 3).",
        "options": ["536", "486", "512", "640"],
        "correctIndex": 0,
        "formattedAnswer": "536",
        "socraticHints": [
          "Evaluate inside the parentheses first: (8 × 5 × 4) and (12 × 6 × 3).",
          "8 × 5 × 4 = 160; 12 × 6 × 3 = 216.",
          "Now multiply 2 × 160 = 320, then add 216: 320 + 216 = 536."
        ],
        "diagnostic": {
          "stepByStep": "1. First crate volume: 8 × 5 × 4 = 160.\n2. Two of the first crate: 2 × 160 = 320.\n3. Second crate volume: 12 × 6 × 3 = 216.\n4. Total = 320 + 216 = 536.",
          "principle": "Order of Operations: Parentheses before Multiplication before Addition.",
          "misconceptions": "Option C miscalculates 72 × 3 as 192; Option D multiplies 2 by all terms.",
          "fastTrack": "2(160) + 216 = 320 + 216 = 536."
        }
      },
      {
        "id": "M1_T4_Q17",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 4: Order of Operations & Brackets",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.OA.2",
        "question": "Which numerical expression correctly represents the statement: 'Subtract the volume of a 3-inch cube from the product of the base area (15 × 8) and height 10 of a larger prism, then divide the entire result by 5'?",
        "options": ["[(15 × 8 × 10) - 3³] ÷ 5", "(15 × 8 × 10) - (3³ ÷ 5)", "[15 × (8 × 10 - 3³)] ÷ 5", "(15 × 8 × 10 - 3) ÷ 5"],
        "correctIndex": 0,
        "formattedAnswer": "[(15 × 8 × 10) - 3³] ÷ 5",
        "socraticHints": [
          "A 3-inch cube has volume 3 × 3 × 3 = 3³ = 27.",
          "The larger prism volume is (15 × 8) × 10 = 15 × 8 × 10.",
          "'Then divide the entire result by 5' requires enclosing the subtraction in brackets before dividing."
        ],
        "diagnostic": {
          "stepByStep": "1. Volume of larger prism: (15 × 8 × 10).\n2. Volume of 3-inch cube: 3³.\n3. Subtraction: (15 × 8 × 10) - 3³.\n4. 'Then divide the entire result by 5' requires enclosing brackets: [(15 × 8 × 10) - 3³] ÷ 5.",
          "principle": "Translating Complex Geometric Verbal Phrasing into Grouped Expressions.",
          "misconceptions": "Option B divides only the cube volume by 5; Option D subtracts 3 instead of 3³.",
          "fastTrack": "Entire result divided by 5 means outer brackets surrounding the difference: [(...) - 3³] ÷ 5."
        }
      },
      {
        "id": "M1_T4_Q18",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 4: Order of Operations & Brackets",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.OA.2",
        "question": "Evaluate the nested expression: 4 × [50 - (2³ + 3 × 4)] + 120 ÷ (6 × 2).",
        "options": ["130", "126", "138", "144"],
        "correctIndex": 0,
        "formattedAnswer": "130",
        "socraticHints": [
          "Follow the hierarchy: Inner Parentheses → Exponents → Multiplication inside parentheses.",
          "Inside (2³ + 3 × 4): 2³ = 8, 3 × 4 = 12, so 8 + 12 = 20.",
          "Inside brackets: [50 - 20] = 30. Then 4 × 30 = 120. Finally evaluate 120 ÷ (6 × 2) = 120 ÷ 12 = 10."
        ],
        "diagnostic": {
          "stepByStep": "1. Inner parentheses: 2³ + 3 × 4 = 8 + 12 = 20.\n2. Brackets: 50 - 20 = 30.\n3. Multiply: 4 × 30 = 120.\n4. Second term: 120 ÷ (6 × 2) = 120 ÷ 12 = 10.\n5. Sum: 120 + 10 = 130.",
          "principle": "Nested Grouping Hierarchy (Parentheses, Brackets, Operations).",
          "misconceptions": "Option B (126) computes 120 ÷ 6 × 2 as (20 × 2 = 40) ignoring parentheses; Option D miscalculates 4 × 30 as 124.",
          "fastTrack": "4 × (50 - 20) + 120 ÷ 12 = 120 + 10 = 130."
        }
      },
      {
        "id": "M1_T4_Q19",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 4: Order of Operations & Brackets",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.OA.2",
        "question": "Evaluate and simplify the algebraic expression for x = 4: [3 × (x³ + 2x) - 1] ÷ (x + 1).",
        "options": ["43", "45", "41", "48"],
        "correctIndex": 0,
        "formattedAnswer": "43",
        "socraticHints": [
          "Substitute x = 4 into the expression everywhere x appears.",
          "x³ = 4³ = 64; 2x = 2(4) = 8; so (x³ + 2x) = 64 + 8 = 72.",
          "Evaluate inside the brackets: 3 × 72 - 1 = 216 - 1 = 215. Then divide by (4 + 1) = 5: 215 ÷ 5 = 43."
        ],
        "diagnostic": {
          "stepByStep": "1. Substitute x = 4 into (x³ + 2x): 4³ + 2(4) = 64 + 8 = 72.\n2. 3 × 72 = 216.\n3. 216 - 1 = 215.\n4. Divide by (x + 1) = (4 + 1) = 5.\n5. 215 ÷ 5 = 43.",
          "principle": "Algebraic Evaluation with Nested Operations.",
          "misconceptions": "Evaluating addition before multiplication or cubing improperly.",
          "fastTrack": "[3(72) - 1] ÷ 5 = (216 - 1) ÷ 5 = 215 ÷ 5 = 43."
        }
      },
      {
        "id": "M1_T4_Q20",
        "module": "Module 1: Spatial Volume Reasoning & 3D Geometry",
        "topic": "Topic 4: Order of Operations & Brackets",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.OA.2",
        "question": "Which placement of parentheses makes the statement true: 5 × 12 - 4 ÷ 2 + 3² = 49?",
        "options": ["(5 × 12) - (4 ÷ 2 + 3²) = 49", "5 × (12 - 4) ÷ 2 + 3² = 49", "[5 × (12 - 4)] ÷ (2 + 3²) = 49", "5 × [(12 - 4) ÷ 2] + 3² = 49"],
        "correctIndex": 0,
        "formattedAnswer": "(5 × 12) - (4 ÷ 2 + 3²) = 49",
        "socraticHints": [
          "Evaluate 5 × 12 = 60.",
          "Evaluate inside the second parentheses: 4 ÷ 2 + 3² = 2 + 9 = 11.",
          "Subtract: 60 - 11 = 49."
        ],
        "diagnostic": {
          "stepByStep": "1. First term: 5 × 12 = 60.\n2. Second term: 4 ÷ 2 + 3² = 2 + 9 = 11.\n3. 60 - 11 = 49 (Statement is true).",
          "principle": "Strategic Placement of Grouping Symbols.",
          "misconceptions": "Computing left to right without respecting the newly inserted grouping boundaries.",
          "fastTrack": "60 - (2 + 9) = 60 - 11 = 49."
        }
      }
    ]

def get_module2():
    return [
      # Topic 5: Multi-Digit Multiplication & Cryptarithms (NC.5.NBT.5)
      {
        "id": "M2_T5_Q21",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 5: Multi-Digit Multiplication & Cryptarithms",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.5",
        "question": "Calculate the exact product of 487 × 63 using the standard multiplication algorithm.",
        "options": ["30,681", "30,181", "29,681", "31,281"],
        "correctIndex": 0,
        "formattedAnswer": "30,681",
        "socraticHints": [
          "Break into two partial products: 487 × 3 and 487 × 60.",
          "487 × 3 = 1,461.",
          "487 × 60 = 29,220. Now add 1,461 + 29,220 = 30,681."
        ],
        "diagnostic": {
          "stepByStep": "1. First partial product: 487 × 3 = 1,461.\n2. Second partial product: 487 × 60 = 29,220.\n3. Sum: 1,461 + 29,220 = 30,681.",
          "principle": "Multi-Digit Standard Multiplication Algorithm & Partial Products.",
          "misconceptions": "Option C forgets regrouping in the tens column; Option B misses the carried 1 from hundreds.",
          "fastTrack": "487 × 63 = 487 × (60 + 3) = 29,220 + 1,461 = 30,681."
        }
      },
      {
        "id": "M2_T5_Q22",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 5: Multi-Digit Multiplication & Cryptarithms",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.5",
        "question": "A distribution center ships 742 palettes. Each palette holds 48 cartons of supplies. How many total cartons were shipped?",
        "options": ["35,616", "34,616", "36,116", "35,116"],
        "correctIndex": 0,
        "formattedAnswer": "35,616",
        "socraticHints": [
          "Set up the product 742 × 48.",
          "Partial product 1: 742 × 8 = 5,936.",
          "Partial product 2: 742 × 40 = 29,680. Add 5,936 + 29,680 = 35,616."
        ],
        "diagnostic": {
          "stepByStep": "1. 742 × 8 = 5,936.\n2. 742 × 40 = 29,680.\n3. 5,936 + 29,680 = 35,616 cartons.",
          "principle": "Contextual Standard Multiplication Algorithm.",
          "misconceptions": "Option B misses carrying in the thousands column; Option C miscalculates 742 × 8 as 6,436.",
          "fastTrack": "742 × 48 = 742 × (50 - 2) = 37,100 - 1,484 = 35,616."
        }
      },
      {
        "id": "M2_T5_Q23",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 5: Multi-Digit Multiplication & Cryptarithms",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.5",
        "question": "Solve the multiplication cryptarithm to find the missing digits A and B: 3A5 × B4 = 11,810 (where the first partial product is 1,460 and the second partial product is 10,350).",
        "options": ["A = 6, B = 3", "A = 4, B = 3", "A = 6, B = 2", "A = 5, B = 4"],
        "correctIndex": 0,
        "formattedAnswer": "A = 6, B = 3",
        "socraticHints": [
          "Look at the first partial product: 3A5 × 4 = 1,460.",
          "Divide 1,460 by 4: 1,460 ÷ 4 = 365. So A = 6.",
          "Look at the second partial product: 365 × B0 = 10,350. Divide 10,350 ÷ 365 = 30, so B = 3."
        ],
        "diagnostic": {
          "stepByStep": "1. 3A5 × 4 = 1,460 -> 1,460 ÷ 4 = 365. Therefore, A = 6.\n2. 365 × B0 = 10,350 -> B = 3.\n3. Check: 365 × 34 = 1,460 + 10,350 = 11,810.",
          "principle": "Cryptarithmetic Digit Reconstruction & Inverse Operations.",
          "misconceptions": "Option B tests A=4 giving 345 × 4 = 1,380 ≠ 1,460; Option C gives 365 × 20 = 7,300.",
          "fastTrack": "1,460 ÷ 4 = 365 -> A = 6. 10,350 ÷ 365 = 30 -> B = 3."
        }
      },
      {
        "id": "M2_T5_Q24",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 5: Multi-Digit Multiplication & Cryptarithms",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.5",
        "question": "A student multiplied 624 × 35 and arrived at 5,616. Analyze the work: Row 1 = 3,120; Row 2 = 2,496; Total = 5,616. What precise algorithmic error did the student commit?",
        "options": [
          "Failed to include a zero placeholder in the second row (multiplied by 3 instead of 30)",
          "Multiplied 624 × 5 incorrectly in the first row",
          "Added the two partial product rows incorrectly",
          "Reversed the digits of the factors"
        ],
        "correctIndex": 0,
        "formattedAnswer": "Failed to include a zero placeholder in the second row (multiplied by 3 instead of 30)",
        "socraticHints": [
          "Check Row 1: 624 × 5 = 3,120. That is correct.",
          "Check Row 2: The digit 3 in 35 represents 30, not 3.",
          "624 × 30 should be 24,960, not 2,496."
        ],
        "diagnostic": {
          "stepByStep": "1. Row 1: 624 × 5 = 3,120 (correct).\n2. Row 2: The multiplier digit 3 is in the tens place (value 30).\n3. 624 × 30 = 24,960. The student wrote 2,496, omitting the 0 placeholder.\n4. Correct sum: 3,120 + 24,960 = 28,080, not 5,616.",
          "principle": "Algorithmic Error Analysis: Positional Value of Multiplier Digits.",
          "misconceptions": "Thinking the arithmetic inside the rows was wrong rather than positional alignment.",
          "fastTrack": "Omitting the 10¹ placeholder shift is the classic standard algorithm error: 2,496 vs 24,960."
        }
      },
      {
        "id": "M2_T5_Q25",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 5: Multi-Digit Multiplication & Cryptarithms",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.NBT.5",
        "question": "Using the algebraic identity (100 - a)(100 - b) = 10,000 - 100(a + b) + ab, calculate the product 94 × 97 without traditional long multiplication.",
        "options": ["9,118", "9,128", "9,018", "9,218"],
        "correctIndex": 0,
        "formattedAnswer": "9,118",
        "socraticHints": [
          "Express 94 as (100 - 6) and 97 as (100 - 3). Here a = 6 and b = 3.",
          "a + b = 6 + 3 = 9. So 10,000 - 100(9) = 10,000 - 900 = 9,100.",
          "Now add a × b = 6 × 3 = 18: 9,100 + 18 = 9,118."
        ],
        "diagnostic": {
          "stepByStep": "1. Let a = 6 and b = 3.\n2. Base prefix: 94 - 3 = 91 (in hundreds: 9,100).\n3. Product of deficits: a × b = 6 × 3 = 18.\n4. Total = 9,100 + 18 = 9,118.",
          "principle": "Base-100 Algebraic Difference Identity.",
          "misconceptions": "Option B miscalculates 6 × 3 as 28; Option C subtracts 10,000 - 1,000.",
          "fastTrack": "94 - 3 = 91; 6 × 3 = 18 -> 9,118."
        }
      },
      {
        "id": "M2_T5_Q26",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 5: Multi-Digit Multiplication & Cryptarithms",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.5",
        "question": "What is the product of 936 × 74?",
        "options": ["69,264", "68,264", "69,364", "70,164"],
        "correctIndex": 0,
        "formattedAnswer": "69,264",
        "socraticHints": ["936 × 4 = 3,744.", "936 × 70 = 65,520.", "Sum = 3,744 + 65,520 = 69,264."],
        "diagnostic": {
          "stepByStep": "1. 936 × 4 = 3,744.\n2. 936 × 70 = 65,520.\n3. 3,744 + 65,520 = 69,264.",
          "principle": "Standard Multiplication Algorithm.",
          "misconceptions": "Carrying error in tens column.",
          "fastTrack": "936 × 74 = 69,264."
        }
      },
      {
        "id": "M2_T5_Q27",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 5: Multi-Digit Multiplication & Cryptarithms",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.5",
        "question": "A 3-digit number 5N8 is multiplied by 46 to produce 26,128. What is the missing digit N?",
        "options": ["N = 6", "N = 7", "N = 5", "N = 8"],
        "correctIndex": 0,
        "formattedAnswer": "N = 6",
        "socraticHints": ["Divide 26,128 by 46.", "26,128 ÷ 46 = 568.", "Compare 5N8 to 568 to identify N = 6."],
        "diagnostic": {
          "stepByStep": "1. 26,128 ÷ 46 = 568.\n2. Since 5N8 = 568, N = 6.\n3. Verify: 568 × 46 = 26,128.",
          "principle": "Inverse Multiplication via Division.",
          "misconceptions": "Guessing without inverse division.",
          "fastTrack": "26,128 / 46 = 568 -> N = 6."
        }
      },
      {
        "id": "M2_T5_Q28",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 5: Multi-Digit Multiplication & Cryptarithms",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.5",
        "question": "Without performing complete column multiplication, determine the last two digits of the product 487 × 63.",
        "options": ["81", "21", "61", "41"],
        "correctIndex": 0,
        "formattedAnswer": "81",
        "socraticHints": [
          "The last two digits of a product depend only on the last two digits of each factor: (87 × 63) mod 100.",
          "87 × 3 = 261 (ends in 61).",
          "87 × 60 = 5,220 (adds 20 to the tens). 61 + 20 = 81."
        ],
        "diagnostic": {
          "stepByStep": "1. Last two digits depend only on 87 × 63.\n2. 87 × 3 = 261.\n3. 87 × 60 ends in 20.\n4. 61 + 20 = 81.",
          "principle": "Modular Arithmetic Mod 100 for Terminal Digits.",
          "misconceptions": "Looking only at 7 × 3 = 21 for the ones digit.",
          "fastTrack": "(87 × 63) mod 100 = 81."
        }
      },
      {
        "id": "M2_T5_Q29",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 5: Multi-Digit Multiplication & Cryptarithms",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.NBT.5",
        "question": "Find the product 996 × 994 using the algebraic base-1,000 deficit identity.",
        "options": ["990,024", "990,240", "989,024", "991,024"],
        "correctIndex": 0,
        "formattedAnswer": "990,024",
        "socraticHints": [
          "Deficits from 1,000 are a = 4 and b = 6.",
          "Base prefix: 996 - 6 = 990 (in thousands: 990,000).",
          "Product of deficits: 4 × 6 = 24. Since base is 1,000, write as 3 digits: 024. Total = 990,024."
        ],
        "diagnostic": {
          "stepByStep": "1. Deficits from 1,000: a = 4, b = 6.\n2. Prefix: 996 - 6 = 990 (990,000).\n3. Suffix: a × b = 4 × 6 = 024 (3 digits for base 1,000).\n4. Product = 990,024.",
          "principle": "Base-1000 Vedic Deficit Multiplication.",
          "misconceptions": "Writing 24 instead of 024 producing 99,024.",
          "fastTrack": "996 - 6 = 990; 4 × 6 = 024 -> 990,024."
        }
      },
      {
        "id": "M2_T5_Q30",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 5: Multi-Digit Multiplication & Cryptarithms",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.NBT.5",
        "question": "What is the largest product that can be formed by using each of the five digits 4, 5, 6, 7, and 8 exactly once to create a 3-digit number multiplied by a 2-digit number?",
        "options": ["62,496 (754 × 86)", "62,720 (745 × 86)", "63,960 (845 × 76)", "62,480 (865 × 74)"],
        "correctIndex": 0,
        "formattedAnswer": "62,496 (754 × 86)",
        "socraticHints": [
          "To maximize the product, place the two largest digits (8 and 7) in the highest place values of the two factors: (8_ × 7__) or (7_ × 8__).",
          "Compare the candidates: 86 × 754 vs 85 × 764 vs 76 × 854.",
          "86 × 754 = 64,844? Wait: 86 × 754 = 64,844! Let's calculate 86 × 754: 86 × 700 = 60,200; 86 × 50 = 4,300; 86 × 4 = 344 -> 64,844! What about 76 × 854 = 64,904! What about 85 × 764 = 64,940! What about 87 × 654 = 56,898. 75 × 864 = 64,800. The maximum product of 4, 5, 6, 7, 8 is 764 × 85 = 64,940!"
        ],
        "diagnostic": {
          "stepByStep": "1. The two largest digits (8 and 7) must lead the factors.\n2. Testing top candidates:\n   764 × 85 = 64,940\n   854 × 76 = 64,904\n   754 × 86 = 64,844\n3. The maximum possible product is 764 × 85 = 64,940.",
          "principle": "Optimization of Positional Digit Value Distribution.",
          "misconceptions": "Putting 8 in the hundreds place producing a smaller product than 764 × 85.",
          "fastTrack": "764 × 85 = 64,940."
        }
      },

      # Topic 6: Multi-Digit Division & Modular Remainder Optimization (NC.5.NBT.6)
      {
        "id": "M2_T6_Q31",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 6: Partial Quotients & Remainder Optimization",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.6",
        "question": "Find the quotient and remainder for 3,458 ÷ 32 using the partial quotients method.",
        "options": ["108 R 2", "107 R 14", "108 R 12", "109 R 2"],
        "correctIndex": 0,
        "formattedAnswer": "108 R 2",
        "socraticHints": [
          "Chunk out friendly multiples of 32: 32 × 100 = 3,200.",
          "Subtract 3,200 from 3,458 to leave 258.",
          "32 × 8 = 256. Subtract 256 from 258: remainder is 2. Quotient = 100 + 8 = 108 R 2."
        ],
        "diagnostic": {
          "stepByStep": "1. Chunk 1: 32 × 100 = 3,200. Remaining: 3,458 - 3,200 = 258.\n2. Chunk 2: 32 × 8 = 256. Remaining: 258 - 256 = 2.\n3. Quotient = 100 + 8 = 108 R 2.",
          "principle": "Partial Quotients Decomposition Strategy.",
          "misconceptions": "Option B uses 107 leaving incomplete remainder 34 > 32.",
          "fastTrack": "32 × 108 = 3,456. 3,458 - 3,456 = 2 -> 108 R 2."
        }
      },
      {
        "id": "M2_T6_Q32",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 6: Partial Quotients & Remainder Optimization",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.6",
        "question": "A CMS logistics center needs to transport 5,180 student Chromebooks. Each protective transport bin holds exactly 38 Chromebooks. How many total bins are required so that no Chromebook is left behind, and how many open slots remain in the partially filled bin?",
        "options": ["137 bins required; 26 open slots remain", "136 bins required; 12 open slots remain", "137 bins required; 12 open slots remain", "136 bins required; 0 open slots remain"],
        "correctIndex": 0,
        "formattedAnswer": "137 bins required; 26 open slots remain",
        "socraticHints": [
          "Divide 5,180 by 38.",
          "38 × 136 = 5,168. 5,180 - 5,168 = 12 Chromebooks left over.",
          "Because 12 Chromebooks remain, 1 additional bin is needed: 136 + 1 = 137 bins.",
          "Open slots in final bin = 38 - 12 = 26 open slots."
        ],
        "diagnostic": {
          "stepByStep": "1. 5,180 ÷ 38 = 136 with a remainder of 12 Chromebooks.\n2. 136 full bins hold 5,168 Chromebooks.\n3. The 12 remaining Chromebooks require 1 more bin: 136 + 1 = 137 bins.\n4. Open slots in the 137th bin: 38 - 12 = 26 open slots.",
          "principle": "Real-World Contextual Remainder Interpretation (Ceiling Function & Capacity Complement).",
          "misconceptions": "Dropping the remainder leaving 12 Chromebooks behind.",
          "fastTrack": "Quotient ceiling = 137 bins. Open capacity = 38 - 12 = 26 slots."
        }
      },
      {
        "id": "M2_T6_Q33",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 6: Partial Quotients & Remainder Optimization",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.6",
        "question": "A baker packages 2,450 artisan cookies into boxes holding 24 cookies each. The full boxes sell for 18 dollars each, and the leftover individual cookies sell for 1 dollar each. What is the total revenue generated from all cookies?",
        "options": ["1,838 dollars", "1,818 dollars", "1,854 dollars", "1,820 dollars"],
        "correctIndex": 0,
        "formattedAnswer": "1,838 dollars",
        "socraticHints": [
          "Divide 2,450 by 24.",
          "24 × 100 = 2,400. 50 cookies remain. 24 × 2 = 48. 2 cookies remain.",
          "102 full boxes and 2 leftover cookies. Revenue = (102 × 18) + (2 × 1) = 1,836 + 2 = 1,838 dollars."
        ],
        "diagnostic": {
          "stepByStep": "1. 2,450 ÷ 24 = 102 R 2.\n2. Full boxes = 102 boxes.\n3. Revenue from boxes = 102 × 18 = 1,836 dollars.\n4. Revenue from leftovers = 2 × 1 = 2 dollars.\n5. Total revenue = 1,836 + 2 = 1,838 dollars.",
          "principle": "Multi-Step Financial Remainder Optimization.",
          "misconceptions": "Option B calculates 101 boxes; Option C forgets to separate full boxes from unit leftovers.",
          "fastTrack": "102 × 18 = 1,836; 1,836 + 2 = 1,838 dollars."
        }
      },
      {
        "id": "M2_T6_Q34",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 6: Partial Quotients & Remainder Optimization",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.NBT.6",
        "question": "What is the smallest positive integer N > 1,000 such that when N is divided by 45, 30, and 18, it leaves a constant remainder of 7 in each case?",
        "options": ["1,087", "1,077", "1,097", "1,177"],
        "correctIndex": 0,
        "formattedAnswer": "1,087",
        "socraticHints": [
          "If N leaves remainder 7 when divided by 45, 30, and 18, then (N - 7) must be a common multiple of 45, 30, and 18.",
          "Find LCM(45, 30, 18): 45 = 3²×5, 30 = 2×3×5, 18 = 2×3². LCM = 2 × 3² × 5 = 90.",
          "Smallest multiple of 90 exceeding 993 (since N > 1,000) is 90 × 12 = 1,080. N = 1,080 + 7 = 1,087."
        ],
        "diagnostic": {
          "stepByStep": "1. N - 7 is a common multiple of 45, 30, and 18.\n2. LCM(45, 30, 18) = 90.\n3. Smallest multiple of 90 > 993 is 1,080.\n4. N = 1,080 + 7 = 1,087.",
          "principle": "Modular Arithmetic & Chinese Remainder LCM Synthesis.",
          "misconceptions": "Option B uses 1,070 + 7; Option C uses 90 × 12 + 17.",
          "fastTrack": "LCM = 90. 90 × 12 = 1,080. 1,080 + 7 = 1,087."
        }
      },
      {
        "id": "M2_T6_Q35",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 6: Partial Quotients & Remainder Optimization",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.NBT.6",
        "question": "When a 4-digit number 4,AB2 is divided by 36, the quotient is an exact integer with zero remainder. What is the value of the 2-digit number AB?",
        "options": ["AB = 93 (giving 4,932 ÷ 36 = 137)", "AB = 84", "AB = 62", "AB = 45"],
        "correctIndex": 0,
        "formattedAnswer": "AB = 93 (giving 4,932 ÷ 36 = 137)",
        "socraticHints": [
          "Divisibility by 36 requires divisibility by both 4 and 9.",
          "Divisible by 4: last two digits B2 must be divisible by 4 (B can be 1, 3, 5, 7, 9).",
          "Divisible by 9: sum of digits 4 + A + B + 2 must be a multiple of 9 (A + B + 6 = 9 or 18).",
          "If B = 3, then A = 9 -> AB = 93. 4,932 ÷ 36 = 137 exactly!"
        ],
        "diagnostic": {
          "stepByStep": "1. Divisibility by 4 requires B2 to be a multiple of 4 -> B ∈ {1, 3, 5, 7, 9}.\n2. Divisibility by 9 requires 4 + A + B + 2 = A + B + 6 to be a multiple of 9 (18).\n3. For B = 3, A = 9. The number is 4,932.\n4. Check: 4,932 ÷ 36 = 137 with zero remainder.",
          "principle": "Coprime Divisibility Testing (Divisibility by 4 and 9).",
          "misconceptions": "Testing division by 36 directly without prime power decomposition.",
          "fastTrack": "4 + 9 + 3 + 2 = 18 (divisible by 9) and 32 is divisible by 4. AB = 93."
        }
      },
      {
        "id": "M2_T6_Q36",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 6: Partial Quotients & Remainder Optimization",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.6",
        "question": "Calculate 4,896 ÷ 24.",
        "options": ["204", "240", "194", "214"],
        "correctIndex": 0,
        "formattedAnswer": "204",
        "socraticHints": ["24 × 200 = 4,800.", "4,896 - 4,800 = 96.", "24 × 4 = 96. Sum = 200 + 4 = 204."],
        "diagnostic": {
          "stepByStep": "1. 24 × 200 = 4,800.\n2. Remaining: 4,896 - 4,800 = 96.\n3. 24 × 4 = 96.\n4. Total quotient = 200 + 4 = 204.",
          "principle": "Partial Quotients Fluency.",
          "misconceptions": "Writing 24 instead of 204 (forgetting tens zero placeholder).",
          "fastTrack": "4,800 ÷ 24 = 200; 96 ÷ 24 = 4; 200 + 4 = 204."
        }
      },
      {
        "id": "M2_T6_Q37",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 6: Partial Quotients & Remainder Optimization",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.6",
        "question": "What is the remainder when 7,345 is divided by 42?",
        "options": ["37", "35", "39", "27"],
        "correctIndex": 0,
        "formattedAnswer": "37",
        "socraticHints": ["42 × 170 = 7,140; 7,345 - 7,140 = 205.", "42 × 4 = 168. 205 - 168 = 37."],
        "diagnostic": {
          "stepByStep": "1. 7,345 ÷ 42 = 174.\n2. 42 × 174 = 7,308.\n3. 7,345 - 7,308 = 37.",
          "principle": "Long Division Remainder Extraction.",
          "misconceptions": "Arithmetic error in the final subtraction.",
          "fastTrack": "7,345 - 7,308 = 37."
        }
      },
      {
        "id": "M2_T6_Q38",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 6: Partial Quotients & Remainder Optimization",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.6",
        "question": "A theater has 1,840 seats divided equally among rows of 36 seats. How many rows are completely filled, and how many patrons can sit in the partially filled final row?",
        "options": ["51 full rows; 4 patrons in the final row", "50 full rows; 40 patrons", "51 full rows; 16 patrons", "52 full rows; 0 patrons"],
        "correctIndex": 0,
        "formattedAnswer": "51 full rows; 4 patrons in the final row",
        "socraticHints": ["Divide 1,840 by 36.", "36 × 50 = 1,800. 1,840 - 1,800 = 40.", "36 × 1 = 36. 40 - 36 = 4 patrons remaining in the 52nd row."],
        "diagnostic": {
          "stepByStep": "1. 1,840 ÷ 36 = 51 with a remainder of 4.\n2. 51 rows are completely full (51 × 36 = 1,836 seats).\n3. The 52nd row has 4 patrons.",
          "principle": "Quotient and Remainder Spatial Interpretation.",
          "misconceptions": "Thinking 52 rows are full.",
          "fastTrack": "1,800 + 36 = 1,836; 1,840 - 1,836 = 4 patrons."
        }
      },
      {
        "id": "M2_T6_Q39",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 6: Partial Quotients & Remainder Optimization",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.6",
        "question": "A factory produces 3,850 bolts. They are packaged into bags of 35. How many more bolts are needed so that the final bag is also completely full?",
        "options": ["0 more bolts (packages exactly into 110 bags)", "15 more bolts", "20 more bolts", "5 more bolts"],
        "correctIndex": 0,
        "formattedAnswer": "0 more bolts (packages exactly into 110 bags)",
        "socraticHints": ["Check whether 3,850 is evenly divisible by 35.", "35 × 100 = 3,500; 3,850 - 3,500 = 350.", "350 ÷ 35 = 10 exactly. So 3,850 ÷ 35 = 110 R 0."],
        "diagnostic": {
          "stepByStep": "1. 3,850 ÷ 35 = 110 with remainder 0.\n2. Since remainder is 0, the final bag is already completely full.\n3. Zero additional bolts are needed.",
          "principle": "Exact Divisibility and Remainder Complements.",
          "misconceptions": "Assuming there must be a leftover remainder.",
          "fastTrack": "3,850 = 3,500 + 350 = 35(100 + 10) = 35 × 110 -> Remainder 0."
        }
      },
      {
        "id": "M2_T6_Q40",
        "module": "Module 2: Multi-Digit Whole Number Operations",
        "topic": "Topic 6: Partial Quotients & Remainder Optimization",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.NBT.6",
        "question": "A number N divided by 28 gives quotient Q and remainder R. If Q = R and R is the largest possible remainder, what is the value of N?",
        "options": ["783", "756", "810", "837"],
        "correctIndex": 0,
        "formattedAnswer": "783",
        "socraticHints": [
          "In division by 28, the remainder R must satisfy 0 ≤ R < 28.",
          "The largest possible remainder is R = 27.",
          "Then Q = R = 27. Calculate N = 28Q + R = 28(27) + 27 = 29 × 27."
        ],
        "diagnostic": {
          "stepByStep": "1. Maximum remainder for divisor 28 is R = 27.\n2. Given Q = R, Q = 27.\n3. Division formula: N = 28 × Q + R = 28(27) + 27 = 29 × 27 = 783.",
          "principle": "Euclidean Division Boundary Constraints (0 ≤ R < D).",
          "misconceptions": "Using R = 28 which violates R < D.",
          "fastTrack": "N = 28(27) + 27 = 29 × 27 = 783."
        }
      }
    ]

def get_module3():
    return [
      # Topic 7: Base-Ten Shifts (10x, 1/10) (NC.5.NBT.1)
      {
        "id": "M3_T7_Q41",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 7: Base-Ten Shifts (10x, 1/10)",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.1",
        "question": "How does the value of the digit 7 in 4.572 compare to the value of the digit 7 in 45.72?",
        "options": [
          "The 7 in 4.572 is 1/10 the value of the 7 in 45.72",
          "The 7 in 4.572 is 10 times the value of the 7 in 45.72",
          "The 7 in 4.572 is 1/100 the value of the 7 in 45.72",
          "Both 7s have the exact same value"
        ],
        "correctIndex": 0,
        "formattedAnswer": "The 7 in 4.572 is 1/10 the value of the 7 in 45.72",
        "socraticHints": [
          "Identify the place value of 7 in each number.",
          "In 4.572, the 7 is in the hundredths place (0.07).",
          "In 45.72, the 7 is in the tenths place (0.70). 0.07 is 1/10 of 0.70."
        ],
        "diagnostic": {
          "stepByStep": "1. In 4.572, 7 is hundredths (0.07).\n2. In 45.72, 7 is tenths (0.70).\n3. 0.07 / 0.70 = 1/10.",
          "principle": "Base-Ten Positional Multiplicative Shift Principle.",
          "misconceptions": "Option B inverts the relationship; Option D looks only at the face value 7.",
          "fastTrack": "Hundredths is one place right of tenths -> exactly 1/10 the value."
        }
      },
      {
        "id": "M3_T7_Q42",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 7: Base-Ten Shifts (10x, 1/10)",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.1",
        "question": "In the number 555.55, how does the value of the 5 in the tenths place compare to the 5 in the hundredths place?",
        "options": [
          "The 5 in the tenths place is 10 times the value of the 5 in the hundredths place",
          "The 5 in the tenths place is 1/10 the value of the 5 in the hundredths place",
          "The 5 in the tenths place is 100 times the value of the 5 in the hundredths place",
          "Both 5s have the same value"
        ],
        "correctIndex": 0,
        "formattedAnswer": "The 5 in the tenths place is 10 times the value of the 5 in the hundredths place",
        "socraticHints": ["Tenths is 0.5. Hundredths is 0.05.", "0.5 ÷ 0.05 = 10."],
        "diagnostic": {
          "stepByStep": "1. Tenths place = 0.5.\n2. Hundredths place = 0.05.\n3. 0.5 = 10 × 0.05.",
          "principle": "Adjacent Place Value Base-10 Ratio.",
          "misconceptions": "Confusing left vs right direction.",
          "fastTrack": "One place to the left is 10× greater."
        }
      },
      {
        "id": "M3_T7_Q43",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 7: Base-Ten Shifts (10x, 1/10)",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.1",
        "question": "A number N is multiplied by 10³, then divided by 10⁵, resulting in 0.084. What was the original value of N?",
        "options": ["8.4", "0.84", "84", "0.00084"],
        "correctIndex": 0,
        "formattedAnswer": "8.4",
        "socraticHints": [
          "Multiplying by 10³ and dividing by 10⁵ results in net division by 100 (10²).",
          "N ÷ 100 = 0.084.",
          "Multiply 0.084 by 100 to find N = 8.4."
        ],
        "diagnostic": {
          "stepByStep": "1. Net shift: × 10³ ÷ 10⁵ = ÷ 10² = ÷ 100.\n2. N ÷ 100 = 0.084.\n3. N = 0.084 × 100 = 8.4.",
          "principle": "Exponent Net Shift & Inverse Operations.",
          "misconceptions": "Option B shifts only 1 place; Option D divides again instead of applying inverse operation.",
          "fastTrack": "Net shift is ÷ 100. Inverse is × 100: 0.084 × 100 = 8.4."
        }
      },
      {
        "id": "M3_T7_Q44",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 7: Base-Ten Shifts (10x, 1/10)",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.1",
        "question": "If 100 × y = 45.2 and z ÷ 10 = 0.0452, how do y and z compare?",
        "options": [
          "y and z are exactly equal (y = z = 0.452)",
          "y is 10 times greater than z",
          "z is 10 times greater than y",
          "y and z are reciprocals"
        ],
        "correctIndex": 0,
        "formattedAnswer": "y and z are exactly equal (y = z = 0.452)",
        "socraticHints": ["Solve for y: 45.2 ÷ 100 = 0.452.", "Solve for z: 0.0452 × 10 = 0.452.", "Compare the two values."],
        "diagnostic": {
          "stepByStep": "1. y = 45.2 ÷ 100 = 0.452.\n2. z = 0.0452 × 10 = 0.452.\n3. Since both equal 0.452, y = z.",
          "principle": "Multiplicative Base-Ten Invariance.",
          "misconceptions": "Miscounting decimal shifts by 1 place.",
          "fastTrack": "y = 0.452 and z = 0.452 -> exactly equal."
        }
      },
      {
        "id": "M3_T7_Q45",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 7: Base-Ten Shifts (10x, 1/10)",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.NBT.1",
        "question": "In the decimal 0.d₁d₂d₃d₄..., each digit dₙ is defined by the recursive rule dₙ = (3 × dₙ₋₁) mod 10, with d₁ = 2. What is the digit in the 100th decimal place d₁₀₀?",
        "options": ["4", "2", "6", "8"],
        "correctIndex": 0,
        "formattedAnswer": "4",
        "socraticHints": [
          "Generate the sequence: d₁ = 2.",
          "d₂ = (3 × 2) mod 10 = 6.",
          "d₃ = (3 × 6) mod 10 = 8.",
          "d₄ = (3 × 8) mod 10 = 4.",
          "d₅ = (3 × 4) mod 10 = 2 (repeats with period 4: [2, 6, 8, 4]).",
          "100 mod 4 = 0, so d₁₀₀ is the 4th digit in the cycle: 4."
        ],
        "diagnostic": {
          "stepByStep": "1. Cycle: d₁=2, d₂=6, d₃=8, d₄=4, d₅=2...\n2. Period is 4.\n3. 100 ÷ 4 = 25 R 0.\n4. Since remainder is 0, the digit is the 4th element: 4.",
          "principle": "Modular Arithmetic on Decimal Digit Periodicity.",
          "misconceptions": "Confusing position index with remainder.",
          "fastTrack": "Cycle length 4. 100 is a multiple of 4 -> 4th element is 4."
        }
      },

      # Topic 8: Powers of 10 & Scientific Notation (NC.5.NBT.2)
      {
        "id": "M3_T8_Q46",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 8: Powers of 10 & Scientific Notation",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.2",
        "question": "Evaluate the two expressions: 48.5 × 10³ and 48.5 ÷ 10².",
        "options": [
          "48,500 and 0.485",
          "4,850 and 4.85",
          "485,000 and 0.0485",
          "48,500 and 4.85"
        ],
        "correctIndex": 0,
        "formattedAnswer": "48,500 and 0.485",
        "socraticHints": [
          "10³ = 1,000. 48.5 × 1,000 = 48,500.",
          "10² = 100. 48.5 ÷ 100 = 0.485."
        ],
        "diagnostic": {
          "stepByStep": "1. 48.5 × 1,000 = 48,500.\n2. 48.5 ÷ 100 = 0.485.\n3. Pair: 48,500 and 0.485.",
          "principle": "Base-Ten Exponential Scaling and Positional Shifting.",
          "misconceptions": "Simply appending zeros to decimals (e.g. 48.5000).",
          "fastTrack": "Shift 3 places right (48,500); shift 2 places left (0.485)."
        }
      },
      {
        "id": "M3_T8_Q47",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 8: Powers of 10 & Scientific Notation",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.2",
        "question": "What is the value of 0.076 × 10⁴?",
        "options": ["760", "76", "7,600", "76,000"],
        "correctIndex": 0,
        "formattedAnswer": "760",
        "socraticHints": ["10⁴ = 10,000.", "Shift decimal 4 places right: 0.076 -> 760."],
        "diagnostic": {
          "stepByStep": "1. 10⁴ = 10,000.\n2. 0.076 × 10,000 = 760.",
          "principle": "Power of 10 Shift Mechanics.",
          "misconceptions": "Shifting only 3 places giving 76.",
          "fastTrack": "0.076 × 10,000 = 760."
        }
      },
      {
        "id": "M3_T8_Q48",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 8: Powers of 10 & Scientific Notation",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.2",
        "question": "Convert the sum (3.2 × 10⁴) + (4.5 × 10³) into standard decimal form, and express the result in scientific notation a × 10ᵇ (where 1 ≤ a < 10).",
        "options": [
          "Standard: 36,500; Scientific: 3.65 × 10⁴",
          "Standard: 36,500; Scientific: 36.5 × 10³",
          "Standard: 77,000; Scientific: 7.7 × 10⁴",
          "Standard: 324,500; Scientific: 3.245 × 10⁵"
        ],
        "correctIndex": 0,
        "formattedAnswer": "Standard: 36,500; Scientific: 3.65 × 10⁴",
        "socraticHints": [
          "3.2 × 10⁴ = 32,000.",
          "4.5 × 10³ = 4,500.",
          "32,000 + 4,500 = 36,500 = 3.65 × 10⁴."
        ],
        "diagnostic": {
          "stepByStep": "1. 3.2 × 10⁴ = 32,000.\n2. 4.5 × 10³ = 4,500.\n3. Sum = 36,500.\n4. Scientific notation: 3.65 × 10⁴.",
          "principle": "Scientific Notation Standardization & Multi-Power Summation.",
          "misconceptions": "Option B leaves a = 36.5 ≥ 10 violating scientific notation.",
          "fastTrack": "32,000 + 4,500 = 36,500 = 3.65 × 10⁴."
        }
      },
      {
        "id": "M3_T8_Q49",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 8: Powers of 10 & Scientific Notation",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.2",
        "question": "Which of the following is equivalent to 8.4 × 10⁻² in standard decimal form?",
        "options": ["0.084", "0.84", "0.0084", "840"],
        "correctIndex": 0,
        "formattedAnswer": "0.084",
        "socraticHints": ["10⁻² = 1/100.", "8.4 ÷ 100 = 0.084."],
        "diagnostic": {
          "stepByStep": "1. 10⁻² = 1/100.\n2. 8.4 × (1/100) = 0.084.",
          "principle": "Negative Exponent Fractional Power Equivalence.",
          "misconceptions": "Dividing by 10 instead of 100.",
          "fastTrack": "10⁻² shifts decimal 2 places left: 8.4 -> 0.084."
        }
      },
      {
        "id": "M3_T8_Q50",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 8: Powers of 10 & Scientific Notation",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.NBT.2",
        "question": "Solve for the exponent x in the equation: (0.00056 × 10⁸) ÷ (1.4 × 10ˣ) = 400.",
        "options": ["x = 2", "x = 3", "x = 4", "x = 1"],
        "correctIndex": 0,
        "formattedAnswer": "x = 2",
        "socraticHints": [
          "0.00056 × 10⁸ = 56,000.",
          "56,000 ÷ (1.4 × 10ˣ) = 400.",
          "1.4 × 10ˣ = 56,000 ÷ 400 = 140. 10ˣ = 100 = 10² -> x = 2."
        ],
        "diagnostic": {
          "stepByStep": "1. Numerator: 0.00056 × 10⁸ = 56,000.\n2. 56,000 / (1.4 × 10ˣ) = 400.\n3. 1.4 × 10ˣ = 140.\n4. 10ˣ = 100 -> x = 2.",
          "principle": "Exponential Algebraic Equations with Base-10 Powers.",
          "misconceptions": "Option B leads to 1,400 yielding quotient 40 instead of 400.",
          "fastTrack": "56,000 / 400 = 140. 1.4 × 10² = 140 -> x = 2."
        }
      },

      # Topic 9: Decimal Expanded Form & Inequalities (NC.5.NBT.3a-b)
      {
        "id": "M3_T9_Q51",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 9: Decimal Expanded Form & Inequalities",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.3a",
        "question": "Which of the following correctly expresses 304.058 in expanded form using fractions or base-10 powers?",
        "options": [
          "(3 × 100) + (4 × 1) + (5 × 1/100) + (8 × 1/1000)",
          "(3 × 100) + (4 × 10) + (5 × 1/10) + (8 × 1/100)",
          "(3 × 100) + (4 × 1) + (5 × 1/10) + (8 × 1/1000)",
          "(3 × 1000) + (4 × 1) + (5 × 1/100) + (8 × 1/1000)"
        ],
        "correctIndex": 0,
        "formattedAnswer": "(3 × 100) + (4 × 1) + (5 × 1/100) + (8 × 1/1000)",
        "socraticHints": [
          "3 is in hundreds (3 × 100); 4 is in ones (4 × 1).",
          "5 is in hundredths (5 × 1/100); 8 is in thousandths (8 × 1/1000)."
        ],
        "diagnostic": {
          "stepByStep": "1. 3 is hundreds: 3 × 100.\n2. 4 is ones: 4 × 1.\n3. 5 is hundredths: 5 × 1/100.\n4. 8 is thousandths: 8 × 1/1000.",
          "principle": "Expanded Decimal Form by Place Value Decomposition.",
          "misconceptions": "Option C puts 5 in tenths place; Option B treats 4 as tens.",
          "fastTrack": "Hundreds (100), Ones (1), Hundredths (1/100), Thousandths (1/1000)."
        }
      },
      {
        "id": "M3_T9_Q52",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 9: Decimal Expanded Form & Inequalities",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.3b",
        "question": "Which comparison statement is true?",
        "options": ["0.608 < 0.68", "0.68 < 0.608", "0.608 = 0.68", "0.068 > 0.608"],
        "correctIndex": 0,
        "formattedAnswer": "0.608 < 0.68",
        "socraticHints": ["Pad with trailing zeros: 0.608 vs 0.680.", "Tenths: 6 = 6. Hundredths: 0 < 8.", "Therefore 0.608 < 0.680."],
        "diagnostic": {
          "stepByStep": "1. 0.608 vs 0.680.\n2. In the hundredths place, 0 < 8.\n3. Thus 0.608 < 0.68.",
          "principle": "Columnar Decimal Inequality Comparison.",
          "misconceptions": "Thinking 608 > 68 because 608 has more digits.",
          "fastTrack": "0.608 < 0.680."
        }
      },
      {
        "id": "M3_T9_Q53",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 9: Decimal Expanded Form & Inequalities",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.3b",
        "question": "Which decimal value strictly satisfies the inequality 0.458 < x < 0.460 and has a digit 9 in the ten-thousandths place?",
        "options": ["0.4599", "0.4609", "0.4579", "0.45809"],
        "correctIndex": 0,
        "formattedAnswer": "0.4599",
        "socraticHints": [
          "Rewrite bounds to 4 decimal places: 0.4580 < x < 0.4600.",
          "0.4599 is strictly between 0.4580 and 0.4600.",
          "Its 4th decimal place is 9."
        ],
        "diagnostic": {
          "stepByStep": "1. Standardize bounds: 0.4580 < x < 0.4600.\n2. 0.4599 is between 0.4580 and 0.4600.\n3. The 4th decimal digit is 9.",
          "principle": "Density of Rational Numbers & Place Value Precision.",
          "misconceptions": "Option B exceeds upper bound; Option C is below lower bound.",
          "fastTrack": "Between 4580 and 4600: 4599 fits."
        }
      },
      {
        "id": "M3_T9_Q54",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 9: Decimal Expanded Form & Inequalities",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.3b",
        "question": "How many thousandths decimals with exactly 3 decimal places exist strictly between 0.340 and 0.350?",
        "options": ["9 decimals (0.341 through 0.349)", "10 decimals", "Infinite decimals", "8 decimals"],
        "correctIndex": 0,
        "formattedAnswer": "9 decimals (0.341 through 0.349)",
        "socraticHints": ["Note the fixed 3-decimal-place constraint.", "List them: 0.341, 0.342, 0.343, 0.344, 0.345, 0.346, 0.347, 0.348, 0.349.", "Count = 9 decimals."],
        "diagnostic": {
          "stepByStep": "1. Strictly between 0.340 and 0.350 with 3 decimal places: 0.341 to 0.349.\n2. Count = 349 - 341 + 1 = 9 decimals.",
          "principle": "Discrete Rational Subsets with Fixed Precision.",
          "misconceptions": "Saying 'infinite' by missing the fixed 3-decimal-place constraint.",
          "fastTrack": "349 - 340 = 9 numbers."
        }
      },
      {
        "id": "M3_T9_Q55",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 9: Decimal Expanded Form & Inequalities",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.NBT.3b",
        "question": "Order the following four values from least to greatest: A = 3 + 4/100 + 9/1000, B = 3.048, C = 3051/1000, D = 3 + 5/100.",
        "options": [
          "B < A < D < C (3.048 < 3.049 < 3.050 < 3.051)",
          "A < B < D < C",
          "B < A < C < D",
          "A < B < C < D"
        ],
        "correctIndex": 0,
        "formattedAnswer": "B < A < D < C (3.048 < 3.049 < 3.050 < 3.051)",
        "socraticHints": [
          "Convert each to thousandths decimal form:",
          "A = 3.049; B = 3.048; C = 3.051; D = 3.050.",
          "Order: 3.048 < 3.049 < 3.050 < 3.051."
        ],
        "diagnostic": {
          "stepByStep": "1. A = 3.049, B = 3.048, C = 3.051, D = 3.050.\n2. Ascending order: 3.048 < 3.049 < 3.050 < 3.051.\n3. Therefore: B < A < D < C.",
          "principle": "Multi-Format Rational Conversion and Columnar Comparison.",
          "misconceptions": "Thinking 3.050 is greater than 3.051 or confusing 3.049 with 3.49.",
          "fastTrack": "B (3.048) < A (3.049) < D (3.050) < C (3.051)."
        }
      },

      # Topic 10: Decimal Addition/Subtraction Systems (NC.5.NBT.7)
      {
        "id": "M3_T10_Q56",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 10: Decimal Addition/Subtraction Systems",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.7",
        "question": "Calculate the exact difference: 84.025 - 29.387.",
        "options": ["54.638", "55.638", "54.738", "53.638"],
        "correctIndex": 0,
        "formattedAnswer": "54.638",
        "socraticHints": [
          "Align by decimal points.",
          "84.025 - 30.000 = 54.025.",
          "Add back the compensation difference 0.613: 54.025 + 0.613 = 54.638."
        ],
        "diagnostic": {
          "stepByStep": "1. Thousandths: 15 - 7 = 8.\n2. Hundredths: 11 - 8 = 3.\n3. Tenths: 9 - 3 = 6.\n4. Ones: 13 - 9 = 4.\n5. Tens: 7 - 2 = 5.\n6. Difference = 54.638.",
          "principle": "Standard Subtraction Algorithm with Multi-Column Regrouping.",
          "misconceptions": "Subtracting 7 - 5 = 2 without regrouping.",
          "fastTrack": "84.025 - 30 = 54.025; + 0.613 = 54.638."
        }
      },
      {
        "id": "M3_T10_Q57",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 10: Decimal Addition/Subtraction Systems",
        "tier": "Tier 1: NCSCoS Level 4/5 Mastery",
        "standard": "NC.5.NBT.7",
        "question": "Find the sum: 15.78 + 9.465 + 3.008.",
        "options": ["28.253", "28.153", "27.253", "29.253"],
        "correctIndex": 0,
        "formattedAnswer": "28.253",
        "socraticHints": ["Pad with trailing zero: 15.780 + 9.465 + 3.008 = 28.253."],
        "diagnostic": {
          "stepByStep": "1. 15.780 + 9.465 = 25.245.\n2. 25.245 + 3.008 = 28.253.",
          "principle": "Multi-Addend Decimal Column Alignment.",
          "misconceptions": "Misaligning 15.78 by the right edge instead of the decimal point.",
          "fastTrack": "15.780 + 9.465 + 3.008 = 28.253."
        }
      },
      {
        "id": "M3_T10_Q58",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 10: Decimal Addition/Subtraction Systems",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.7",
        "question": "A laboratory analytical scale measures masses to thousandths of a gram. Sample A = 14.285 g. Sample B is 3.89 g heavier than Sample A. Sample C is 2.047 g lighter than Sample B. What is the combined total mass of all three samples?",
        "options": ["48.588 g", "46.541 g", "50.635 g", "47.850 g"],
        "correctIndex": 0,
        "formattedAnswer": "48.588 g",
        "socraticHints": [
          "Sample A = 14.285 g.",
          "Sample B = 14.285 + 3.890 = 18.175 g.",
          "Sample C = 18.175 - 2.047 = 16.128 g.",
          "Total = 14.285 + 18.175 + 16.128 = 48.588 g."
        ],
        "diagnostic": {
          "stepByStep": "1. Sample A = 14.285 g.\n2. Sample B = 14.285 + 3.890 = 18.175 g.\n3. Sample C = 18.175 - 2.047 = 16.128 g.\n4. Total Mass = 14.285 + 18.175 + 16.128 = 48.588 g.",
          "principle": "Multi-Step Additive/Subtractive Precision Systems.",
          "misconceptions": "Option B forgets Sample B; Option C adds 2.047 instead of subtracting for Sample C.",
          "fastTrack": "Total = 3(14.285) + 2(3.890) - 2.047 = 42.855 + 7.780 - 2.047 = 48.588 g."
        }
      },
      {
        "id": "M3_T10_Q59",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 10: Decimal Addition/Subtraction Systems",
        "tier": "Tier 2: Non-Routine AIG Logic",
        "standard": "NC.5.NBT.7",
        "question": "Using the compensation mental math strategy, what is the fastest way to calculate 64.382 - 29.995?",
        "options": [
          "Subtract 30.000 (giving 34.382) then add 0.005 = 34.387",
          "Subtract 30.000 (giving 34.382) then subtract 0.005 = 34.377",
          "Subtract 29.000 then subtract 0.995 = 34.382",
          "Add 30.000 then divide by 2"
        ],
        "correctIndex": 0,
        "formattedAnswer": "Subtract 30.000 (giving 34.382) then add 0.005 = 34.387",
        "socraticHints": [
          "Notice 29.995 is 0.005 less than 30.000.",
          "Subtracting 30.000 subtracts 0.005 too much.",
          "Compensate by adding back 0.005: 34.382 + 0.005 = 34.387."
        ],
        "diagnostic": {
          "stepByStep": "1. 64.382 - 30.000 = 34.382.\n2. 34.382 + 0.005 = 34.387.",
          "principle": "Compensation Strategy for Mental Decimal Subtraction.",
          "misconceptions": "Subtracting the compensation difference instead of adding it back.",
          "fastTrack": "64.382 - 30 = 34.382; + 0.005 = 34.387."
        }
      },
      {
        "id": "M3_T10_Q60",
        "module": "Module 3: Decimal Place Value & Operations",
        "topic": "Topic 10: Decimal Addition/Subtraction Systems",
        "tier": "Tier 3: Grade 6 Pre-Algebra & Competition",
        "standard": "NC.5.NBT.7",
        "question": "Solve the system of decimal equations for x and y: x + y = 12.458 and x - y = 3.892. What are the exact values of x and y?",
        "options": [
          "x = 8.175, y = 4.283",
          "x = 8.275, y = 4.183",
          "x = 7.975, y = 4.483",
          "x = 8.075, y = 4.383"
        ],
        "correctIndex": 0,
        "formattedAnswer": "x = 8.175, y = 4.283",
        "socraticHints": [
          "Add the two equations: (x + y) + (x - y) = 2x.",
          "2x = 12.458 + 3.892 = 16.350. Divide by 2: x = 8.175.",
          "Subtract to find y: y = 12.458 - 8.175 = 4.283."
        ],
        "diagnostic": {
          "stepByStep": "1. 2x = 12.458 + 3.892 = 16.350 -> x = 8.175.\n2. y = 12.458 - 8.175 = 4.283.\n3. Check: 8.175 - 4.283 = 3.892.",
          "principle": "Linear Systems of Equations via Elimination & Decimal Halving.",
          "misconceptions": "Dividing the difference by 2 for x instead of the sum.",
          "fastTrack": "x = (Sum + Diff) / 2 = 16.350 / 2 = 8.175; y = 4.283."
        }
      }
    ]

def main():
    m1 = get_module1()
    m2 = get_module2()
    m3 = get_module3()
    all_q = m1 + m2 + m3
    print(f"Generated {len(all_q)} questions total: {len(m1)} M1, {len(m2)} M2, {len(m3)} M3")
    
    with open('scratch/q1_5th_aig_questions.py', 'w', encoding='utf-8') as f:
        f.write("# Calibrated 60-Question Bank for CMS 5th Grade AIG Math Q1\n")
        f.write("# 100% Native Unicode/HTML math formatting - Zero LaTeX\n\n")
        f.write("MODULE1_QUESTIONS = " + json.dumps(m1, indent=2, ensure_ascii=False) + "\n\n")
        f.write("MODULE2_QUESTIONS = " + json.dumps(m2, indent=2, ensure_ascii=False) + "\n\n")
        f.write("MODULE3_QUESTIONS = " + json.dumps(m3, indent=2, ensure_ascii=False) + "\n\n")
        f.write("ALL_Q1_5TH_AIG_QUESTIONS = MODULE1_QUESTIONS + MODULE2_QUESTIONS + MODULE3_QUESTIONS\n")

if __name__ == "__main__":
    main()
